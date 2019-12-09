from .input_reader.reader import Reader
from .functions.triangular import Triangular
from .fuzzy.region import Region
from .graphics.plot_region import plot_region
import pandas as pd

## CONSTANTS
# PLAYER_SIZE = 0.3
# PLAYER_BODY = 0.085

# KM = 0.7
# PMV = 1.2*1.05
# KA = (PS + PB + KM)*1.05
# DD = 1.2*2*1.05

#create reader with default data path values
reader = Reader()

#create fuzzy input regions
## input 1: distance from player to ball
dist_minor = Region('D3', 1000, 0, 100, Triangular(10, 20, 15, 1, 0).function)
dist_fair = Region('D2', 1000, 0, 100, Triangular(10, 20, 15, 1, 0).function)
dist_great = Region('D1', 1000, 0, 100, Triangular(10, 20, 15, 1, 0).function)
distance = [dist_minor, dist_fair, dist_great]

## input 2: relative speed from ball to player
rspeed_minor = Region('RS3', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
rspeed_fair = Region('RS2', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
rspeed_great = Region('RS1', 100, 0, 30, Triangular(10, 20, 15, 1, 0).function)
relative_speed = [rspeed_minor, rspeed_fair, rspeed_great]

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
    print(distance.max())