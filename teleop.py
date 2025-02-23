import cv2
import tqdm
from lerobot.common.utils.utils import say
from robot import robot, safe_connect

with safe_connect(robot, release_torque=True):
    seconds = 120
    frequency = 200

    # for _ in tqdm.tqdm(range(seconds*frequency)):
    #     leader_pos = robot.leader_arms["main"].read("Present_Position")
    #     robot.follower_arms["main"].write("Goal_Position", leader_pos)
    say(f"正在启动遥控模式，预计持续 {seconds} 秒")
    for _ in tqdm.tqdm(range(seconds * frequency), desc="遥控中"):
        observation, action = robot.teleop_step(record_data=True)
        for key in observation:
            if "image" in key:
                cv2.imshow(
                    key, cv2.cvtColor(observation[key].numpy(), cv2.COLOR_RGB2BGR)
                )
        cv2.waitKey(1)

    say("注意！将在 5 秒后释放力矩")
    for _ in tqdm.tqdm(range(5 * frequency), desc="即将释放从臂力矩"):
        robot.teleop_step()

    for arm in robot.follower_arms.values():
        arm.write("Torque_Enable", 0)
