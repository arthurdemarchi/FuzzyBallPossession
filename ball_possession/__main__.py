from .input_reader.reader import Reader
from .functions.triangular import Triangular
from .functions.trapezoid import Trapezoid
from .fuzzy.region import Region
from .graphics.plot_region import plot_region
import pandas as pd

## CONSTANTS
PS = 0.3 # PLAYER_SIZE
PB = 0.085 # PLAYER_BODY
CPD = PS+PB # CERTAIN POSSESSION DISTANCE
KR = 0.7 # KICKABLE RADIUS
KA = (PS + PB + KR)*1.05 # KICKABLE AREA
DD = 1.2*2*1.05 # DASHABLE DISTANCE
PMS = 1.2*1.05 # PLAYER MAXIMUM SPEED
RS = (2*KA)/1.5 # REACTION SPEED

#create reader with default data path values
reader = Reader()

#create fuzzy input regions
## input 1: distance from player to ball
dist_minor = Region('D3', 1000, 0, 100, Trapezoid(0, 1.5*CPD, 0, CPD).function)
dist_fair = Region('D2', 1000, 0, 100, Triangular(CPD, 1.5*KA, KA).function)
dist_great = Region('D1', 1000, 0, 100, Trapezoid(KA, 100, DD, 100).function)
distance = [dist_minor, dist_fair, dist_great]

## input 2: relative speed from ball to player
rspeed_minor = Region('RS3', 50, 0, 5, Trapezoid(0, 1.5*RS, 0, RS).function)
rspeed_great = Region('RS1', 50, 0, 5, Trapezoid(RS, 5, 1.5*RS, 5).function)
relative_speed = [rspeed_minor, rspeed_great]

## input 3: ball absolute speed
bspeed_minor = Region('BS3', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
bspeed_fair = Region('BS2', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
bspeed_great = Region('BS1', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
ball_speed = [bspeed_minor, bspeed_fair, bspeed_minor]

# output
## ball possession
bposs_minor = Region('BP3', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
bposs_fair = Region('BP2', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
bposs_great = Region('BP1', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
ball_possession = [bposs_minor, bposs_fair, bposs_great]

#while there's a file to read run application
status = True
while status:
    status, distance, relative_speed, ball_speed = reader.read_next_file()
    print(relative_speed.max())