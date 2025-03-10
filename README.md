基于Python计算机视觉和ADB的《部落冲突》智能自动化系统，支持全分辨率适配多种模拟器
无需Root即可实现资源收集、兵种管理等核心功能。

🏰 COC Robot - 部落冲突自动化助手
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![ADB Required](https://img.shields.io/badge/ADB-34.0.5+-orange.svg)](https://developer.android.com/studio/releases/platform-tools)

!!![部落冲突自动化演示](images/demo.gif)


🌟 核心功能

| 功能模块         | 支持特性                                                                 |
|------------------|-------------------------------------------------------------------------|
| 🔄 资源收集       | 自动识别金币/圣水/黑油，智能规避障碍物                                   |
| 🐉 兵种管理       | 雷龙/气球批量捐赠，训练队列自动补兵                                      |
| 🖥️ 多分辨率适配   | 动态适配 720P/1080P/2K 设备                                             |
| 🚨 异常处理       | 断线重连/弹窗拦截/操作失败自动重试                                       |

🚀 快速开始

### 环境要求
- Windows 10/11 64位
- 雷电模拟器 9.0+ ([下载地址](https://www.ldmnq.com))
- Python 3.9+ ([下载地址](https://www.python.org/downloads/))

### 五分钟部署指南

1. **配置模拟器**
    - 安装雷电模拟器
   # 创建新实例
   - 分辨率: 1080x2400
   - DPI: 440
   - 开启: USB调试/ROOT权限

2. **安装依赖**
    ```bash
    curl -O https://dl.google.com/android/repository/platform-tools-latest-windows.zip
    unzip platform-tools-latest-windows.zip
    ```
    将ADB工具添加至系统环境变量
    在终端运行以下命令查看是否成功连接设备
    ```bash
    adb devices
    ```
    将连接到的设备名在`config.py`文件内配置

    git clone https://github.com/yourname/COC_robot.git
    cd COC_robot
    pip install -r requirements.txt

    或使用VSCODE自带的conda创建虚拟环境

3. **ADB连接验证**
    adb devices
    # 在config.py中配置设备ID

4. **首次运行**
   python command.py --function command_1  # 测试全局识别功能

⚙️ 核心配置

    设备配置文件 (config.py)
    # ADB 路径配置
    adb_path = 'C:/platform-tools/adb.exe'  # ← 修改为实际路径

    # 设备分辨率模式
    DEVICE_PROFILES = {
    0: {'name': '1080P', 'size': (1080, 2400)},
    1: {'name': '720P',  'size': (720, 1280)}
    }

    模板管理系统
    modle/
    ├── UI_Elements/
    │   ├── collect/      # 资源收集相关模板
    │   ├── donate/       # 兵种捐赠相关模板
    │   └── system/       # 系统界面模板
    └── sample_template.png  # 模板制作规范示例

🛠️ 高级使用
    ### 添加新模板
    1. 截取游戏界面元素（推荐使用ADB截图）
    2. 将图片保存到`modle`目录
    3. 在`template_labels.py`注册新模板
    ```python
    template_labels = {
        'new_template.png': True,
        #...
    }

    ### 单独功能测试
    python command.py --function donate  # 测试捐兵功能
    python command.py --function collect # 测试资源收集功能

    ### 自定义手势操作
    # 在adb_swipe_utils.py中扩展手势库
    def custom_swipe_pattern():
        multi_touch_zoom(
            start_x1=300, start_y1=800, 
            end_x1=500, end_y1=500,
            steps=15,  # 增加操作精度
            duration=300
        )
    ### 高级参数调整
    # 在template_match.py中调整匹配参数
    def find_template_position(...,
        threshold=0.75,   # 匹配置信度阈值
        min_scale=0.75,    # 最小缩放比例
        max_scale=2.0,    # 最大缩放比例
        steps=20          # 多尺度检测粒度
    )

🚨 故障排查
    Q: ADB设备未连接
    A: adb kill-server && adb start-server
    # 检查模拟器USB调试开关

    Q: ADB连接不稳定
    A: 1. adb kill-server && adb start-server
       2. 重启模拟器

    Q: 脚本无法识别界面元素
    A: 1. 检查模板图片是否匹配当前分辨率
       2. 单独运行python command.py --function command_1，观察并调试识别效果
       2. 该模版是否成功添加

    Q: 手势操作不生效
    A: 1. # 在adb_swipe_utils.py中调整duration参数
        def swipe_down(duration=800):  # 增加操作时长
            adb_command(f"shell input swipe 250 1000 250 300 {duration}")
       2. 检查操作坐标是否正确

🤝 贡献指南
    我们欢迎以下类型的贡献：
    🎯 新增游戏界面模板
    🧩 优化图像识别算法
    📊 完善测试用例
    📝 补充多语言文档
    请遵循 贡献规范 提交PR。

📄 开源协议
本项目采用 MIT License，请遵守Supercell的[粉丝内容政策](https://www.supercell.com/fan-content-policy)
