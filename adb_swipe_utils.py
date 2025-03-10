import subprocess
import time
import config

def adb_command(command):
    """
    执行 ADB 命令并返回结果。
    """
    cmd = f"{config.adb_path} {command}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Command '{command}' executed successfully.")
    else:
        print(f"Command '{command}' failed with error: {result.stderr}")
    return result

def swipe_up(duration=500):
    """
    向上滑动屏幕。
    """
    adb_command(f"shell input swipe 500 1500 500 500 {duration}")

def swipe_down(duration=500):
    """
    向下滑动屏幕。
    """
    adb_command(f"shell input swipe 250 1000 250 300 {duration}")
    time.sleep(2)

def swipe_left(duration=500):
    """
    向左滑动屏幕。
    """
    adb_command(f"shell input swipe 800 600 200 600 {duration}")
    time.sleep(2)

def swipe_right(duration=500):
    """
    向右滑动屏幕。
    """
    adb_command(f"shell input swipe 100 1000 1000 1000 {duration}")

def send_event(device, type, code, value):
    """
    发送单个事件到设备。
    """
    adb_command(f"shell sendevent {device} {type} {code} {value}")

def multi_touch_zoom(device_path="/dev/input/event2", start_x1=300, start_y1=800, end_x1=500, end_y1=500, 
                     start_x2=700, start_y2=800, end_x2=500, end_y2=500, steps=10, duration=200):
    """
    双指捏合缩放
    - 缩小：双指向内滑动（end 点比 start 点更靠近中心）
    - 放大：双指向外滑动（end 点比 start 点更远离中心）
    """
    # 第一个手指按下（ID=0）
    send_event(device_path, 3, 57, 0)   # ABS_MT_TRACKING_ID
    send_event(device_path, 3, 53, start_x1) # ABS_MT_POSITION_X
    send_event(device_path, 3, 54, start_y1) # ABS_MT_POSITION_Y
    send_event(device_path, 0, 0, 0)    # SYN_REPORT

    # 第二个手指按下（ID=1）
    send_event(device_path, 3, 57, 1)
    send_event(device_path, 3, 53, start_x2)
    send_event(device_path, 3, 54, start_y2)
    send_event(device_path, 0, 0, 0)

    # 双指移动
    for step in range(steps):
        x1 = int(start_x1 + (end_x1 - start_x1) * step / steps)
        y1 = int(start_y1 + (end_y1 - start_y1) * step / steps)
        x2 = int(start_x2 + (end_x2 - start_x2) * step / steps)
        y2 = int(start_y2 + (end_y2 - start_y2) * step / steps)
        
        # 更新第一个手指位置
        send_event(device_path, 3, 53, x1)
        send_event(device_path, 3, 54, y1)
        send_event(device_path, 3, 57, 0)
        send_event(device_path, 0, 0, 0)
        
        # 更新第二个手指位置
        send_event(device_path, 3, 53, x2)
        send_event(device_path, 3, 54, y2)
        send_event(device_path, 3, 57, 1)
        send_event(device_path, 0, 0, 0)
        time.sleep(duration / 1000 / steps)

    # 抬起手指
    send_event(device_path, 3, 57, -1)
    send_event(device_path, 0, 0, 0)
    send_event(device_path, 3, 57, -1)
    send_event(device_path, 0, 0, 0)

def pinch_in(duration=500):
    """
    缩小屏幕。
    """
    multi_touch_zoom(
        start_x1=300, start_y1=800, end_x1=500, end_y1=500,
        start_x2=700, start_y2=800, end_x2=500, end_y2=500,
        duration=duration
    )

def pinch_out(duration=500):
    """
    放大屏幕。
    """
    multi_touch_zoom(
        start_x1=500, start_y1=500, end_x1=300, end_y1=800,
        start_x2=500, start_y2=500, end_x2=700, end_y2=800,
        duration=duration
    )