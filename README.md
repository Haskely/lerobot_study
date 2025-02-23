# Lerobot 学习

## 环境

- System: Windows 11 64 位操作系统, 基于 x64 的处理器
- RAM: 32.0 GB
- CPU: 13th Gen Intel(R) Core(TM) i9-13900K   3.00 GHz
- GPU: NVIDIA GeForce RTX 4090 24G

```bash
uv sync

git clone https://github.com/Haskely/lerobot.git

cd lerobot && git switch haskely && cd ../

uv pip install -e lerobot[dynamixel,pi0,pusht]
```

## 主要文件及使用说明

### 1. 配置文件
- `config.py` - 核心配置文件
  - 定义了机械臂的硬件配置(电机、相机等)
  - 设置数据集相关配置
  - 配置机器人的标定目录

**使用方法：**
```bash
# 首先配置 config.py 中的相关参数，就地修改
```

### 2. 机器人标定与控制
- `robot.py` - 获取控制机器人的核心对象
  - 实现了安全连接的上下文管理器 `safe_connect`
  - 自动处理连接断开和力矩释放

- `reset.py` - 机器人重置脚本
  - 用于重新标定机械臂
  - 需要先删除 .cache 文件夹再运行

**使用方法：**
```bash
# 删除 .cache 文件夹
rm -rf .cache
# 运行重置脚本进行标定
python reset.py
```

### 3. 遥控操作
- `teleop.py` - 遥控操作脚本
  - 实现机器人的遥控功能
  - 支持实时显示相机画面
  - 自动处理力矩释放

**使用方法：**
```bash
# 测试遥控操作
python teleop.py
```

### 4. 数据采集与重放
- `record.py` - 数据采集脚本
  - 右键提前完成当前轮录制
  - 左键重新录制当前轮
  - 使用 ESC 退出录制

- `replay.py` - 数据重放脚本
  - 可以重放已采集的数据
  - 支持设置重放的 episode 编号

**使用方法：**
```bash
# 采集数据
python record.py

# 重放数据
python replay.py
```

### 5. 数据可视化
- `visualize_data.py` - 数据可视化脚本
  - 可视化指定 episode 的数据

- `visualize_html.py` - HTML格式可视化（目前有 BUG，是官方实现的锅）
  - 生成数据的 HTML 可视化页面

**使用方法：**
```bash
python visualize_data.py
```

### 6. 模型训练与部署
- `train.py` - 训练脚本
- `evaluate.py` - 用训好的模型操作机械臂

**使用方法：**
```bash
# 训练模型
wandb login
python train.py

# 部署测试
python evaluate.py
```

## 注意事项

- 使用前请确保正确配置了机器人的硬件参数
- 建议先进行机器人标定再进行其他操作
- 数据采集时注意保存路径的设置
- 遥控操作时要注意机器人的安全范围
