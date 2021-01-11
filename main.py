
from __future__ import print_function
import xbox
import link
import time


def fmtFloat(n):
    return '{: 6.3f}'.format(n)


def show(*args):
    for arg in args:
        print(arg, end="")


def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)


joy = xbox.Joystick()
link.Connect("127.0.0.1", 6000)


def setServoToReady():
    link.SendMessage(0x2101, {"mode": 0})
    link.SendMessage(0x2001, {"robot": 1, "status": 1})


def setRobotEnable():
    link.SendMessage(0x2301, {"deadman": 1})


def setCoordToCart():
    link.SendMessage(0x2201, {"robot": 1, "coord": 1})


def setSpeed(speed):
    link.SendMessage(0x2601, {"robot": 1, "speed": speed})


def setRobotDisable():
    link.SendMessage(0x2301, {"deadman": 0})


def jogRobot(axis, direction):
    link.SendMessage(0x2901, {"axis": axis, "direction": direction})


def stopJog(axis):
    link.SendMessage(0x2902, {"axis": axis})


speed = 5

print("Press Back button to exit")
while not joy.Back():
    # A/B/X/Y buttons
    if joy.leftX() > 0.1:
        jogRobot(2, joy.leftX())
    if joy.leftX() < -0.1:
        jogRobot(2, joy.leftX())
    elif joy.leftX() <= 0.1 and joy.leftX() >= -0.1:
        stopJog(2)
    if joy.leftY() > 0.1:
        jogRobot(1, joy.leftY())
    if joy.leftY() < -0.1:
        jogRobot(1, joy.leftY())
    elif joy.leftY() <= 0.1 and joy.leftY() >= -0.1:
        stopJog(1)
    if joy.rightX() > 0.1:
        jogRobot(4, joy.rightX)
    if joy.rightX() < -0.1:
        jogRobot(4, joy.rightX)
    elif joy.rightX() <= 0.1 and joy.rightX() >= -0.1:
        stopJog(4)
    if joy.rightY() > 0.1:
        jogRobot(5, joy.rightY)
    if joy.rightY() < -0.1:
        jogRobot(5, joy.rightY)
    elif joy.rightY() <= 0.1 and joy.rightY() >= -0.1:
        stopJog(5)
    if joy.dpadUp():
        if speed <= 95:
            speed = speed + 5
            setSpeed(speed)
    if joy.dpadDown():
        if speed >= 5:
            speed = speed - 5
            setSpeed(speed)
    if joy.dpadLeft():
        print("dpadLeft")
    if joy.dpadRight():
        print("dpadRight")
    if joy.A():
        setRobotEnable()
    if joy.B():
        setRobotDisable()
    if joy.X():
        setServoToReady()
    if joy.Y():
        setCoordToCart()
    if joy.leftBumper():
        jogRobot(3, 1)
    if joy.rightBumper():
        jogRobot(3, -1)
    if joy.rightBumper() == 0 and joy.leftBumper() == 0:
        stopJog(3)
    if joy.leftThumbstick():
        print("leftThumbstick")
    if joy.rightThumbstick():
        print("rightThumbstick")
    if joy.leftTrigger():
        jogRobot(6, -1)
    if joy.rightTrigger():
        jogRobot(6, 1)
    if joy.rightTrigger() == 0 and joy.leftTrigger == 0:
        stopJog(6)
    time.sleep(0.1)
    # Move cursor back to start of line
# Close out when done
joy.close()
