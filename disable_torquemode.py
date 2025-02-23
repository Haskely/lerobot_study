from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus, TorqueMode
from config import leader_config, follower_config

leader_arm = DynamixelMotorsBus(leader_config)
follower_arm = DynamixelMotorsBus(follower_config)

leader_arm.connect()
follower_arm.connect()

leader_arm.write("Torque_Enable", TorqueMode.DISABLED.value)
follower_arm.write("Torque_Enable", TorqueMode.DISABLED.value)
