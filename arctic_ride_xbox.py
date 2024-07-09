#LEGO SPIKE ESSENTIAL - let you control Arctic ride vehicle from https://education.lego.com/en-us/lessons/spikeessential-great-adventures/spikeessential-arctic-ride/ 
#using Xbox controller and pybrics. Control via X/Y/A/B buttons

from pybricks.parameters import Direction, Port, Button
from pybricks.pupdevices import Motor
from pybricks.iodevices import XboxController
from pybricks.robotics import Car
from pybricks.tools import wait

left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
remote = XboxController()
velo = 0;
veloAcc = 10;
turnAcc = 7;
turnAngle = 0
runTime = 10;
while True:
    # Read remote state.
    pressed = remote.buttons.pressed()

    print(pressed)
    steering = 0
    if Button.Y in pressed:
        velo = min(velo +veloAcc, 500);
    elif Button.A in pressed:
        velo = max(velo -veloAcc, -500);
    else:
        velo =0    

    if Button.B in pressed:
        turnAngle =max(turnAngle -turnAcc, -300);
    elif Button.X in pressed:
        turnAngle =min(turnAngle +turnAcc, 300);
    else:
        turnAngle =0    

    left.run(velo-turnAngle)
    right.run(velo+turnAngle)    
    # Wait briefly.
    wait(runTime)
    
