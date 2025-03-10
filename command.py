from template_match import match_template_with_options
from template_labels import reset_detected_templates, get_detected_templates
from adb_swipe_utils import swipe_up, swipe_down, swipe_left, swipe_right, pinch_in, pinch_out
import os
import time

# 获取模板图片路径列表
template_dir = 'modle'
template_names = [f for f in os.listdir(
    template_dir) if f.endswith('.png')]


# 第一次识别，不做任何点击，只是识别出有哪些模板，并记录这些模板名，并且标注出这些模板在截图中的位置，可用于调试验证模板是否正确
def command_1():
    for template_name in template_names:
        if match_template_with_options(template_name, click=False, rescreenshot=True):
            print(f"Template {template_name} detected.")
        else:
            print(f"Template {template_name} not detected.")

    # 获取识别到的模板名称
    detected_templates = get_detected_templates()
    print("Detected templates:")
    for template in detected_templates:
        print(template)


# 收集资源
def command_collect():
    if match_template_with_options('heiyoushouji.png', click=True, rescreenshot=True, click_count=1):
        print("成功收集黑油")
    else:
        print("黑油未检测到，收集失败")

    if match_template_with_options('shengshuishouji.png', click=True, rescreenshot=True, click_count=1):
        print("成功收集圣水")
    else:
        print("圣水未检测到，收集失败")

    if match_template_with_options('jinbishouji.png', click=True, rescreenshot=True, click_count=1):
        print("成功收集金币")
    else:
        print("金币未检测到，收集失败")


# 重新加载游戏
def Reload_game():
    if match_template_with_options('chongjin.png', click=True, rescreenshot=True):
        print("正在重新加载游戏")
    else:
        print("不需要重新加载游戏")

    if match_template_with_options('chongjin_1.png', click=True, rescreenshot=True):
        print("正在重新加载游戏")
    else:
        print("不需要重新加载游戏")


# 识别关闭按钮，并点击
def command_closs():
    if match_template_with_options('guanbi_1.png', click=True, rescreenshot=True):
        print("成功关闭当前窗口")
    else:
        print("未检测到关闭按钮")


# 连续3次识别进入游戏中的关闭按钮，并点击
def command_closs_begin():
    counter = 0
    while counter < 3:
        if match_template_with_options('guanbi_2.png', click=True, rescreenshot=True):
            print("成功关闭加载窗口")
        else:
            print("未检测需要关闭的窗口")
        time.sleep(2)
        counter += 1


# 捐兵3下，默认捐雷龙
def command_donate(name='zengyuan_leilong.png'):
    # 确保其余窗口已关闭
    if match_template_with_options('guanbi_1.png', click=True, rescreenshot=True):
        print("成功关闭当前窗口")
    if match_template_with_options('shouqi.png', click=True, rescreenshot=True,roi=(450,250,150,200)):
        print("成功关闭当前窗口")
    else:
        print("未检测到关闭按钮")

    # 通过识别进攻是否存在，确保在大厅主页
    if match_template_with_options('jingong.png', click=False, rescreenshot=True,roi=(0,500,200,200)):
        print("当前在大厅主页，可以进行捐兵操作")
        time.sleep(1)
        if match_template_with_options('xiaoxi.png', click=True, rescreenshot=True, click_count=1,roi=(0, 250, 150, 150)):
            print("已进入聊天窗口")
            time.sleep(1)
            if match_template_with_options('xiaoxi_buluo.png', click=True, rescreenshot=True, click_count=1,roi=(450, 150, 150, 150)):
                print("已进入部落聊天界面")
                time.sleep(1)
                if match_template_with_options('zengyuan.png', click=True, rescreenshot=True, click_count=1,roi=(0,125,480,480)):
                    print("已检测到有人需要捐兵")
                    if match_template_with_options(name, click=True, rescreenshot=True, click_count=3):
                        print("已捐3个兵")
                        time.sleep(1)
                        if match_template_with_options('guanbi_1.png', click=True, rescreenshot=True,roi=(1100,0,100,60)):
                            time.sleep(2)
                            print("成功关闭当前窗口")
                        match_template_with_options('shouqi.png', click=True, rescreenshot=True,roi=(450,250,150,200))
                else:
                    print("向下滑动")
                    swipe_down()
                    if match_template_with_options('zengyuan.png', click=True, rescreenshot=True, click_count=1,roi=(0,125,480,480)):
                        print("已检测到有人需要捐兵")
                        match_template_with_options(name, click=True, rescreenshot=True, click_count=3)
                        print("已捐3个兵")
                        time.sleep(1)
                        if match_template_with_options('guanbi_1.png', click=True, rescreenshot=True,roi=(1100,0,100,60)):
                            time.sleep(2)
                            match_template_with_options('shouqi.png', click=True, rescreenshot=True,roi=(450,250,150,200))
                            print("成功关闭当前窗口")
    else:
        print("当前不在大厅主页，无法进行增援操作")
        match_template_with_options('guanbi_1.png', click=True, rescreenshot=True)
        time.sleep(1)
        match_template_with_options('shouqi.png', click=True, rescreenshot=True,roi=(450,250,150,200))

    if match_template_with_options('guanbi_1.png', click=True, rescreenshot=True):
        print("成功关闭当前窗口")


# 炼兵，自动炼5个兵，默认炼雷龙
def command_practice(name='xunlian_leilong.png'):
    # 确保其余窗口已关闭
    if match_template_with_options('guanbi_1.png', click=True, rescreenshot=True):
        print("成功关闭当前窗口")
    else:
        print("未检测到关闭按钮")

    # 通过识别进攻是否存在，确保在大厅主页
    if match_template_with_options('jingong.png', click=False, rescreenshot=True,roi=(0,500,200,200)):
        print("当前在大厅主页，可以进行炼兵操作")
        time.sleep(1)
        if match_template_with_options('lianbing.png', click=True, rescreenshot=True, click_count=1):
            print("已进入训练场")
            time.sleep(1)
            if match_template_with_options('xunlian_budui.png', click=True, rescreenshot=True, click_count=1):
                print("已进入训练部队界面")
                time.sleep(1)
                if match_template_with_options(name, click=True, rescreenshot=True, click_count=5):
                    print("已进成功训练5个兵")
                    time.sleep(1)
                else:
                    print("向左滑动")
                    swipe_left()
                    swipe_left()
                    match_template_with_options(
                        name, click=True, rescreenshot=True, click_count=5)
                    print("已进成功训练5个兵")
                    time.sleep(1)
    else:
        print("当前不在大厅主页，无法进行炼兵操作。")
        match_template_with_options('guanbi_1.png', click=True, rescreenshot=True)
    if match_template_with_options('guanbi_1.png', click=True, rescreenshot=True):
        print("成功关闭当前窗口")
