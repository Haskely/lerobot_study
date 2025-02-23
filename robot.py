from lerobot.common.robot_devices.robots.manipulator import ManipulatorRobot
from config import robot_config_w_camera


class safe_connect:
    """
    添加上下文管理器，当退出时自动释放力矩并断开连接

    with safe_connect(robot):
        ...
    """

    def __init__(self, robot: ManipulatorRobot, release_torque=False):
        self._robot = robot
        self.release_torque = release_torque

    def __enter__(self):
        self._robot.connect()
        return self._robot

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._robot.is_connected:
            if self.release_torque:
                for name, arm in self._robot.leader_arms.items():
                    print(f"Releasing torque on leader_arms:{name}")
                    arm.write("Torque_Enable", 0)
                for name, arm in self._robot.follower_arms.items():
                    print(f"Releasing torque on follower_arms:{name}")
                    arm.write("Torque_Enable", 0)
            self._robot.disconnect()


robot = ManipulatorRobot(robot_config_w_camera)
