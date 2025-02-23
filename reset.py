"""
先删除 .cache 文件夹，然后运行这个文件，可以重新标定机械臂
"""

from config import robot_config_wo_camera
from lerobot.common.robot_devices.robots.manipulator import ManipulatorRobot

robot = ManipulatorRobot(robot_config_wo_camera)

robot.connect()  # 若没有标定 cache 会自动触发标定
robot.follower_arms["main"].write("Torque_Enable", 0)  # 关闭力矩
robot.disconnect()
