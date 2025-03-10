```markdown
# COC Robot - 部落冲突自动化助手

一个基于ADB和计算机视觉的《部落冲突》自动化脚本，支持资源收集、兵种捐赠、自动训练等功能。无需Root，兼容主流安卓模拟器。

## ✨ 主要功能

- **智能资源收集**  
  自动识别并收集金币/圣水/黑油
- **一键捐兵系统**  
  支持雷龙等兵种快速捐赠（可扩展）
- **兵营自动化管理**  
  捐兵后自动补兵，支持批量训练
- **多分辨率适配**  
  720P/1080P/2K设备开箱即用
- **智能异常处理**  
  自动识别弹窗并重连游戏

## 🛠️ 环境配置

### 前置要求
- Windows 10/11 或 macOS
- 安卓模拟器（推荐[雷电模拟器](https://www.ldmnq.com)）
- Python 3.9+

### 使用步骤
1. 安装ADB工具
   ```bash
   curl -O https://dl.google.com/android/repository/platform-tools-latest-windows.zip
   unzip platform-tools-latest-windows.zip
   ```
2. 克隆本仓库
   ```bash
   git clone https://github.com/helxo0321/COC_robot.git
   cd COC_robot
   ```
3. 安装Python依赖
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ 配置说明

### 基础配置 (`config.py`)
```python
adb_path = 'C:/PATH/platform-tools/adb.exe'  # 修改为你的ADB路径
device_vm_size = 0  # 0: 1080x2400 | 1: 720x1280
```

### 模拟器设置
- 分辨率：1080x2400 (DPI 440)
- 开启USB调试模式
- 性能设置：4核CPU/4096MB内存

## 🖼️ 模板系统

### 现有模板
```
modle/
├── heiyoushouji.png    # 黑油收集按钮
├── zengyuan_leilong.png # 雷龙捐赠图标
├── jingong.png         # 进攻按钮
└── ... (共23个预置模板)
```

### 添加新模板
1. 截取游戏界面元素（推荐使用ADB截图）
2. 将图片保存到`modle`目录
3. 在`template_labels.py`注册新模板
```python
template_labels = {
    'new_template.png': True,
    #...
}
```

## 🚀 使用指南

### 基础操作
```python
# 主程序入口
python main.py

# 单独功能测试
python command.py --function donate  # 测试捐兵功能
python command.py --function collect # 测试资源收集
```

### 高级参数
```python
# 在template_match.py中调整匹配参数
def find_template_position(...,
    threshold=0.75,   # 匹配置信度阈值
    min_scale=0.5,    # 最小缩放比例
    max_scale=2.0,    # 最大缩放比例
    steps=20          # 多尺度检测粒度
)
```

## 📌 注意事项

1. **游戏设置要求**
   - 使用简体中文界面
   - 尽量关闭所有特效和动画
   - 保持游戏缩放比例为默认

2. **性能优化**
   - 为模拟器开启VT虚拟化
   - 关闭Windows Defender实时保护
   - 优先使用雷电模拟器9.0+版本

3. **常见问题**
   ```markdown
   Q: 脚本无法识别界面元素
   A: 1. 检查模板图片是否匹配当前分辨率
      2. 单独运行python command.py --function command_1，观察并调试识别效果

   Q: ADB连接不稳定
   A: 1. adb kill-server && adb start-server
      2. 重启模拟器
   ```

## 🤝 参与贡献
欢迎提交PR或Issue：
1. 添加新的游戏模板
2. 优化手势操作算法
3. 扩展多语言支持

## 📄 开源协议
本项目采用 MIT License，请遵守Supercell的[粉丝内容政策](https://www.supercell.com/fan-content-policy)
```

![操作演示](images/demo.gif)  
*实际运行效果演示*
