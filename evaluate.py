import time
from lerobot.common.policies.act.modeling_act import ACTPolicy
from lerobot.common.robot_devices.utils import busy_wait
import torch
from robot import robot
import cv2

inference_time_s = 60
fps = 30
device = "cuda"  # TODO: On Mac, use "mps" or "cpu"


ckpt_path = r"data\outputs\train\act\checkpoints\040000\pretrained_model"
policy = ACTPolicy.from_pretrained(ckpt_path)

policy.to(device)
policy.eval()
print(f"Model loaded - {ckpt_path}")

with robot as robot:
    print("Robot connected")

    with torch.inference_mode(), torch.no_grad():
        for i in range(inference_time_s * fps):
            start_time = time.perf_counter()

            # Read the follower state and access the frames from the cameras
            observation: dict[str, torch.Tensor] = robot.capture_observation()
            print(f"Observation: {len(observation)}", end="\t")

            # Convert to pytorch format: channel first and float32 in [0,1]
            # with batch dimension
            for name in observation:
                data = observation[name]
                print(
                    f"{name.removeprefix('observation.')}: {list(data.shape)} max:{data.max().item()} min:{data.min().item()}",
                    end="\t",
                )
                if "image" in name:
                    cv2.imshow(name, cv2.cvtColor(data.numpy(), cv2.COLOR_RGB2BGR))
                    data = data.type(torch.float32) / 255
                    data = data.permute(2, 0, 1).contiguous()
                data = data.unsqueeze(0)
                observation[name] = data.to(device)
            cv2.waitKey(1)
            print()

            # Compute the next action with the policy
            # based on the current observation
            print("Inference Action...", end="\t")
            action = policy.select_action(observation)
            print(f"Action: {action.shape}")
            # Remove batch dimension
            action = action.squeeze(0)
            # Move to cpu, if not already the case
            action = action.to("cpu")
            # Order the robot to move
            robot.send_action(action)

            dt_s = time.perf_counter() - start_time
            busy_wait(1 / fps - dt_s)
