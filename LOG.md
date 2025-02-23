# DEBUG

```python
import cv2

# 摄像头索引列表
indexes = [0, 1] # 编号 1 摄像头 报错 [ WARN:0@12.732] global cap_msmf.cpp:1795 CvCapture_MSMF::grabFrame videoio(MSMF): can't grab frame. Error: -2147483638
# indexes = [0] # 正常
# indexes = [1] # 正常
caps = [cv2.VideoCapture(index) for index in indexes]

while True:
    frames = []
    for cap in caps:
        ret, frame = cap.read()
        if not ret:
            frames.append(None)
        else:
            frames.append(frame)

    # 显示每个摄像头的画面
    for i, frame in enumerate(frames):
        if frame is not None:
            cv2.imshow(f'frame {i}', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放所有 VideoCapture 对象
for cap in caps:
    cap.release()

cv2.destroyAllWindows()
```

如上代码，我是windows11系统。我有两个摄像头设备。

当我只链接其中一个时，代码正常工作，我能看到摄像头的实时画面。

当我想同时连接两个时，出现异常！编号 0 摄像头正常工作，但是编号 1 摄像头 报错 [ WARN:0@12.732] global cap_msmf.cpp:1795 CvCapture_MSMF::grabFrame videoio(MSMF): can't grab frame. Error: -2147483638

请分析原因或者如何排查

# 环境配置

```bash
uv venv --seed

git clone
```

# 配置机器

```bash
python lerobot/lerobot/scripts/control_robot.py --robot.type=koch --control.type=teleoperate
```

# 检测摄像头

```bash
python lerobot/lerobot/common/robot_devices/cameras/opencv.py --images-dir outputs/images_from_opencv_cameras
```

# Now run this to record 2 episodes:

```bash
python lerobot/lerobot/scripts/control_robot.py \
  --robot.type=koch \
  --control.type=record \
  --control.single_task="Grasp a lego block and put it in the bin." \
  --control.fps=30 \
  --control.repo_id=Haskely/koch_test \
  --control.tags='["tutorial"]' \
  --control.warmup_time_s=5 \
  --control.episode_time_s=30 \
  --control.reset_time_s=30 \
  --control.num_episodes=1 \
  --control.push_to_hub=false \
  --control.resume=true
```

```bash
python lerobot/lerobot/common/datasets/v2/convert_dataset_v1_to_v2.py \
    --robot koch \
    --repo-id Haskely/koch_test \
    --single-task "TASK DESCRIPTION."
```

```bash
python lerobot/lerobot/scripts/visualize_dataset_html.py --repo-id Haskely/koch_test
```

```bash
python lerobot/lerobot/scripts/visualize_dataset.py \
    --repo-id lerobot/pusht \
    --episode-index 0
```
