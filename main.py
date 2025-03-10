from adb_utils import capture_screen
from template_match import match_template_with_options
from template_labels import reset_detected_templates, get_detected_templates
from adb_swipe_utils import swipe_up, swipe_down, swipe_left, swipe_right, pinch_in, pinch_out
from command import command_1, command_closs, Reload_game, command_collect, command_practice, command_donate
import os
import glob
import time


def clear_directory(directory):
    """
    清空指定目录中的所有文件。
    """
    files = glob.glob(os.path.join(directory, '*'))
    for f in files:
        os.remove(f)


if __name__ == "__main__":
    # 创建结果文件夹
    result_dir = 'modle_result'
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    else:
        # 清空结果文件夹
        clear_directory(result_dir)

    # 删除之前的截屏和结果图片
    if os.path.exists('screen.png'):
        os.remove('screen.png')
    if os.path.exists('result.png'):
        os.remove('result.png')

    # 重置识别到的模板名称
    reset_detected_templates()

    # Reload_game()
    # time.sleep(20)
    # command_closs()

    # command_collect()
    # command_practice(name="xunlian_bingren.png")
    command_donate()


# 执行滑动和缩放操作
# swipe_up()
# swipe_down()
# swipe_left()
# swipe_right()
# pinch_in()
# pinch_out()
