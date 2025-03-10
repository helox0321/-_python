from image_utils import find_template_position
from template_labels import add_detected_template
import cv2
import subprocess
import config
import os
import time

def adb_command(command):
    """
    执行 ADB 命令并返回结果。
    """
    cmd = f"{config.adb_path} {command}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Command '{command}' executed successfully.")
    else:
        print(f"Command '{command}' failed with: {result.stderr}")
    return result

def match_template(template_name, threshold=0.6, click=False):
    """
    通过传入模型图片的名字，与根目录下的截屏文件进行对比，并在截屏图片上标注出模型图片的位置。
    """
    template_path = os.path.join('modle', template_name)
    
    # 读取屏幕截图
    adb_command("shell screencap -p /sdcard/screen.png")
    adb_command("pull /sdcard/screen.png .")
    screenshot_path = 'screen.png'
    screenshot = cv2.imread(screenshot_path)
    if screenshot is None:
        print("Failed to read screenshot.")
        return False
    else:
        print("Screenshot read successfully.")

    # 查找模板位置
    result = find_template_position(screenshot_path, template_path, threshold=threshold)
    
    if result:
        x, y, w, h = result
        print(f"Template {template_name} matched at position: ({x}, {y}), width: {w}, height: {h}")
        # 在截图中绘制矩形
        cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if click:
            # 模拟点击匹配到的位置
            click_x = x + w // 2
            click_y = y + h // 2
            adb_command(f"shell input tap {click_x} {click_y}")
        # 保存结果图片
        result_path = os.path.join('modle_result', f"{template_name}_result.png")
        cv2.imwrite(result_path, screenshot)
        print(f"Result image saved as '{result_path}'.")
        # 记录识别到的模板名称
        add_detected_template(template_name)
        return True
    else:
        print(f"Template {template_name} not found.")
        return False

def match_template_with_options(template_name, click=False, rescreenshot=True, threshold=0.75, min_scale=0.75, max_scale=2.5, click_count=1, roi=None):
    """
    通过传入特定的模板名称，与是否点击，是否重新截图进行模板匹配。
    """
    template_path = os.path.join('modle', template_name)
    screenshot_path = 'screen.png'
    
    # 如果允许重新截图或者没有上一次的截图，则截图
    if rescreenshot or not os.path.exists(screenshot_path):
        adb_command("shell screencap -p /sdcard/screen.png")
        adb_command("pull /sdcard/screen.png .")
    
    # 读取屏幕截图
    screenshot = cv2.imread(screenshot_path)
    if screenshot is None:
        print("Failed to read screenshot.")
        return False
    else:
        print("Screenshot read successfully.")

    # 如果指定了 ROI，则裁剪截图
    if roi:
        roi_x, roi_y, roi_w, roi_h = roi
        screenshot = screenshot[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]
        cv2.imwrite('roi_screen.png', screenshot)
        screenshot_path = 'roi_screen.png'

    # 查找模板位置
    result = find_template_position(screenshot_path, template_path, threshold=threshold, min_scale=min_scale, max_scale=max_scale)
    
    if result:
        x, y, w, h = result
        print(f"Template {template_name} matched at position: ({x}, {y}), width: {w}, height: {h}")
        # 在截图中绘制矩形
        cv2.rectangle(screenshot, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if click:
            # 计算点击位置在大截图中的坐标
            click_x = x + w // 2 + (roi_x if roi else 0)
            click_y = y + h // 2 + (roi_y if roi else 0)
            for _ in range(click_count):
                adb_command(f"shell input tap {click_x} {click_y}")
                time.sleep(0.25)
        # 保存结果图片
        result_path = os.path.join('modle_result', f"{template_name}_result.png")
        cv2.imwrite(result_path, screenshot)
        print(f"Result image saved as '{result_path}'.")
        # 记录识别到的模板名称
        add_detected_template(template_name)
        return True
    else:
        print(f"Template {template_name} not found.")
        return False