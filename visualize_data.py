from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from lerobot.scripts.visualize_dataset import visualize_dataset
from config import record_config

if __name__ == "__main__":
    dataset = dataset = LeRobotDataset(
        record_config.repo_id,
        root=record_config.root,
        local_files_only=record_config.local_files_only,
    )

    visualize_dataset(
        dataset=dataset,
        episode_index=0,
    )
