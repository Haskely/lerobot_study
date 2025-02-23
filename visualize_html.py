from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from lerobot.scripts.visualize_dataset_html import visualize_dataset_html
from config import record_config

if __name__ == "__main__":
    dataset = LeRobotDataset(
        record_config.repo_id,
        root=record_config.root,
        local_files_only=record_config.local_files_only,
    )

    visualize_dataset_html(
        dataset=dataset,
    )
