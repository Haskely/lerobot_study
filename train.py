from lerobot.scripts.train import train, TrainPipelineConfig, init_logging
from lerobot.configs.default import WandBConfig, DatasetConfig
from lerobot.common.policies.act.configuration_act import ACTConfig
from config import dataset_config, DATA_ROOT, DATA_DESC

policy_config = ACTConfig()
# HACK: https://github.com/huggingface/lerobot/blob/fe483b1d0d4ad8506f61924d905943eaa6d3ece0/lerobot/configs/train.py#L76
policy_config.pretrained_path = (
    DATA_ROOT / "outputs/train/act/checkpoints/040000/pretrained_model"
)

train_config = TrainPipelineConfig(
    dataset=DatasetConfig(
        repo_id=dataset_config.repo_id,
        root=dataset_config.root,
        episodes=list(range(9, 20)),
        local_files_only=dataset_config.local_files_only,
    ),
    policy=policy_config,
    output_dir=DATA_ROOT / "outputs/train/act_2",
    job_name=DATA_DESC,
    device="cuda",
    wandb=WandBConfig(
        enable=True,
        project="lerobot",
    ),
    steps=40000,
    save_freq=10000,
)

if __name__ == "__main__":
    import logging

    init_logging()

    # File handler
    train_log_path = train_config.output_dir.with_name(
        f"{train_config.output_dir.name}.log"
    )
    train_log_path.parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(train_log_path, encoding="utf-8")
    logging.getLogger().addHandler(file_handler)

    train(train_config)
