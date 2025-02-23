from lerobot.scripts.control_robot import replay
from config import dataset_config
from robot import robot
from lerobot.common.utils.utils import say
from lerobot.common.robot_devices.control_configs import (
    ReplayControlConfig,
)

replay_config = ReplayControlConfig(
    repo_id=dataset_config.repo_id,
    episode=0,
    root=dataset_config.root,
    fps=30,
    local_files_only=True,
)

if __name__ == "__main__":
    # robot.connect()
    # robot.disconnect()
    say("即将重放数据")
    replay(
        robot=robot,
        cfg=replay_config,
    )
