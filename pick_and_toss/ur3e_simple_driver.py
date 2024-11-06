import rclpy
from std_msgs.msg import Float64

class UR3eArmDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.__shoulder_lift_joint = self.__robot.getDevice('shoulder_lift_joint')
        self.__shoulder_lift_joint.setPosition(-1.57)

        self.__target_shoulder_lift_joint = Float64()

        rclpy.init(args=None)
        self.__node = rclpy.create_node('ur3e_driver')
        self.__node.create_subscription(Float64, 'ur3e/joints/shoulder_lift_joint', self.__shoulder_lift_joint_callback, 1)

    def __shoulder_lift_joint_callback(self, msg):
        self.__target_shoulder_lift_joint = msg
        shoulder_lift_joint = self.__target_shoulder_lift_joint.data
        self.__shoulder_lift_joint.setPosition(shoulder_lift_joint)

    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)
