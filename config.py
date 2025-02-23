from lerobot.configs.train import DatasetConfig
from lerobot.common.robot_devices.robots.configs import KochRobotConfig
from lerobot.common.robot_devices.motors.configs import DynamixelMotorsBusConfig
from lerobot.common.robot_devices.cameras.configs import OpenCVCameraConfig
from pathlib import Path

DATA_ROOT = Path("data")

leader_config = DynamixelMotorsBusConfig(
    port="COM7",
    motors={
        # name: (index, model)
        "shoulder_pan": (1, "xl330-m077"),
        "shoulder_lift": (2, "xl330-m077"),
        "elbow_flex": (3, "xl330-m077"),
        "wrist_flex": (4, "xl330-m077"),
        "wrist_roll": (5, "xl330-m077"),
        "gripper": (6, "xl330-m077"),
    },
)

follower_config = DynamixelMotorsBusConfig(
    port="COM6",
    motors={
        # name: (index, model)
        "shoulder_pan": (1, "xl430-w250"),
        "shoulder_lift": (2, "xl430-w250"),
        "elbow_flex": (3, "xl330-m288"),
        "wrist_flex": (4, "xl330-m288"),
        "wrist_roll": (5, "xl330-m288"),
        "gripper": (6, "xl330-m288"),
    },
)

camera_configs = {
    "top": OpenCVCameraConfig(0, fps=30, width=640, height=480),
    "side": OpenCVCameraConfig(1, fps=30, width=640, height=480),
    "arm": OpenCVCameraConfig(2, fps=30, width=640, height=480),
}

CALIBRATION_DIR = DATA_ROOT / "calibration/koch"
CALIBRATION_DIR.mkdir(parents=True, exist_ok=True)

robot_config_wo_camera = KochRobotConfig(
    leader_arms={"main": leader_config},
    follower_arms={"main": follower_config},
    cameras={},
    calibration_dir=CALIBRATION_DIR,
)

robot_config_w_camera = KochRobotConfig(
    leader_arms={"main": leader_config},
    follower_arms={"main": follower_config},
    cameras=camera_configs,
    calibration_dir=CALIBRATION_DIR,
)

DATASET_DIR = DATA_ROOT / "dataset"
DATASET_DIR.mkdir(parents=True, exist_ok=True)

DATA_NAME = "exam_2"
DATA_DESC = "将篮子放到容器里"
REPO_ID = f"Haskely/{DATA_NAME}"
DATASER_PATH = DATASET_DIR / DATA_NAME

dataset_config = DatasetConfig(
    repo_id=REPO_ID,
    root=DATASER_PATH,
    local_files_only=True,
)
