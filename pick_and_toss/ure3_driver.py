import rclpy
from sensor_msgs.msg import Image
from trajectory_msgs.msg import JointTrajectoryPoint

class URE3Driver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot
        self.__camera1 = self.__robot.getDevice("camera1")
        self.__camera2 = self.__robot.getDevice("camera2")
        self.__shoulder_pan_joint  = self.__robot.getDevice("shoulder_pan_joint")
        self.__shoulder_lift_joint = self.__robot.getDevice("shoulder_lift_joint")
        self.__elbow_joint         = self.__robot.getDevice("elbow_joint")

        self.__camera1.enable(100)
        self.__camera2.enable(100)
        self.__shoulder_pan_joint.setPosition(-1.57)
        self.__shoulder_lift_joint.setPosition(0.78)
        self.__elbow_joint.setPosition(1.57)

        self.__target_shoulder_pan_joint = JointTrajectoryPoint()
        self.__target_shoulder_lift_joint = JointTrajectoryPoint()
        self.__target_elbow_joint = JointTrajectoryPoint()

        rclpy.init(args=None)

        self.__node = rclpy.create_node('ure3_driver')
        self.__node.create_subscription()