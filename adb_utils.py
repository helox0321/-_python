import subprocess
import os
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

def capture_screen():
    """
    截取屏幕截图并保存到根目录。
    """
    # 截取屏幕截图并保存到设备的存储中
    adb_command("shell screencap -p /sdcard/screen.png")
    
    # 将截图从设备的存储中拉取到本地文件系统
    adb_command("pull /sdcard/screen.png .")
    
    # 检查截图是否成功保存到本地
    if os.path.exists("screen.png"):
        print("Screenshot saved successfully.")
    else:
        print("Failed to save screenshot.")