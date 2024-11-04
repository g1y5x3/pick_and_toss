from controller import Robot, Motor
from math import pi, sin


robot = Robot()

timestep = int(robot.getBasicTimeStep())

shoulder_pan_joint = robot.getDevice('shoulder_pan_joint')
shoulder_lift_joint = robot.getDevice('shoulder_lift_joint')
elbow_joint = robot.getDevice('elbow_joint')

shoulder_lift_joint.setPosition(-1.57)
shoulder_pan_joint.setPosition(0.78)
elbow_joint.setPosition(1.57)

while robot.step(timestep) != -1:
    pass
