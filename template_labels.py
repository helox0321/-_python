template_labels = {
    'chongjin_1.png': True,
    'chongjin.png': True,
    'guanbi_1.png': True,
    'guanbi_2.png': True,
    'heiyoushouji.png': True,
    'huiying.png': True,
    'jinbishouji.png': True,
    'jingong.png': True,
    'lianbing.png': True,
    'lingqu.png': True,
    'queding.png': True,
    'shengshuishouji.png': True,
    'shouji.png': True,
    'shoujiche.png': True,
    'shouqi.png': True,
    'xiaoxi_buluo.png': True,
    'xiaoxi.png': True,
    'xunlian_bingren.png': True,
    'xunlian_budui.png': True,
    'xunlian_leilong.png': True,
    'zengyuan_bingren.png': True,
    'zengyuan_leilong.png': True,
    'zengyuan.png': True,
    # 添加更多模板及其标签
}

# 用于记录此次识别到的模板名称
detected_templates = []


def is_label_allowed(template_name):
    """
    检查模板标签是否被允许使用。
    """
    return template_labels.get(template_name, False)


def add_detected_template(template_name):
    """
    添加识别到的模板名称。
    """
    detected_templates.append(template_name)


def reset_detected_templates():
    """
    重置识别到的模板名称。
    """
    global detected_templates
    detected_templates = []


def get_detected_templates():
    """
    获取识别到的模板名称。
    """
    return detected_templates
