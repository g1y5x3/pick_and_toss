from controller import Robot, Camera


robot = Robot()

timestep = int(robot.getBasicTimeStep())

camera1 = robot.getDevice('camera1')
camera2 = robot.getDevice('camera2')

camera1.enable(32)
camera2.enable(32)

while robot.step(timestep) != -1:
    pass
