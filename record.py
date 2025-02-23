"""
右键：提前完成当前轮录制
左键：重新录制当前轮
ESC：退出录制
"""

from lerobot.scripts.control_robot import record
from config import dataset_config, DATA_DESC
from robot import robot, safe_connect
from lerobot.common.robot_devices.control_configs import (
    RecordControlConfig,
)

record_config = RecordControlConfig(
    repo_id=dataset_config.repo_id,
    single_task=DATA_DESC,
    root=dataset_config.root,
    policy=None,
    device=None,
    use_amp=None,
    fps=30,
    warmup_time_s=10,
    episode_time_s=300,
    reset_time_s=3,
    num_episodes=10,
    run_compute_stats=False,
    push_to_hub=False,
    resume=True,
    local_files_only=True,
)

if __name__ == "__main__":
    with safe_connect(robot):
        record(
            robot=robot,
            cfg=record_config,
        )
