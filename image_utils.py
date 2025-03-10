import cv2
import numpy as np

def preprocess_image(image):
    """
    对图像进行预处理，例如灰度化、模糊处理等。
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

def find_template_position(large_image_path, template_image_path, output_path="result.png", threshold=0.6, min_scale=0.5, max_scale=2.0):
    """
    在大图中查找模板图像的位置，并在大图上绘制矩形框。
    """
    # 读取图像并预处理
    large_image = cv2.imread(large_image_path)
    template = cv2.imread(template_image_path)
    
    # 高斯去噪
    large_image = cv2.GaussianBlur(large_image, (3, 3), 0)
    template = cv2.GaussianBlur(template, (3, 3), 0)
    
    # 使用彩色图像
    large_color = large_image.copy()
    template_color = template.copy()
    
    # 多尺度参数
    scales = np.linspace(min_scale, max_scale, 20)  # 在指定范围内搜索20个尺度
    
    best_match = None
    max_val = 0
    
    for scale in scales:
        h, w = template.shape[:2]
        resized_template = cv2.resize(template_color, (int(w * scale), int(h * scale)))
        if resized_template.shape[0] > large_color.shape[0] or resized_template.shape[1] > large_color.shape[1]:
            continue
        
        # 使用彩色匹配
        result = cv2.matchTemplate(large_color, resized_template, cv2.TM_CCOEFF_NORMED)
        _, current_max_val, _, (x, y) = cv2.minMaxLoc(result)
        
        if current_max_val > max_val:
            max_val = current_max_val
            best_match = (x, y, resized_template.shape[1], resized_template.shape[0], scale)
    
    if max_val < threshold:
        print("提示：未找到匹配，请尝试：\n1. 检查模板是否准确\n2. 扩大 scales 范围\n3. 进一步降低 threshold")
        return None
    
    # 标注结果
    x, y, w, h, scale = best_match
    cv2.rectangle(large_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(output_path, large_image)
    print(f"匹配成功！位置：({x}, {y})，缩放比例：{scale:.2f}，置信度：{max_val:.2f}")
    return (x, y, w, h)