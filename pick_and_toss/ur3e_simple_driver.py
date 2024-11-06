import rclpy
from std_msgs.msg import Float64

class UR3eArmDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot

        self.__shoulder_lift_joint = self.__robot.getDevice("shoulder_lift_joint")
        self.__shoulder_pan_joint = self.__robot.getDevice("shoulder_pan_joint")
        self.__elbow_joint = self.__robot.getDevice("elbow_joint")

        self.__shoulder_lift_joint.setPosition(-1.57)
        self.__shoulder_pan_joint.setPosition(0.78)
        self.__elbow_joint.setPosition(1.57)

        rclpy.init(args=None)

        self.__node = rclpy.create_node("ur3e_driver")

        self.__node.create_subscription(Float64, 'ur3e/joints/shoulder_lift_joint', self.__shoulder_lift_joint_callback, 1)
        self.__node.create_subscription(Float64, 'ur3e/joints/shoulder_pan_joint', self.__shoulder_pan_joint_callback, 1)
        self.__node.create_subscription(Float64, 'ur3e/joints/elbow_joint', self.__elbow_joint_callback, 1)

    def __shoulder_lift_joint_callback(self, msg: Float64):
        self.__shoulder_lift_joint.setPosition(msg.data)
    
    def __shoulder_pan_joint_callback(self, msg):
        self.__shoulder_pan_joint.setPosition(msg.data)

    def __elbow_joint_callback(self, msg):
        self.__elbow_joint.setPosition(msg.data)

    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)
