from .input_reader.reader import Reader
from .functions.triangular import Triangular
from .functions.trapezoid import Trapezoid
from .fuzzy.region import Region
from .graphics.plot_region import plot_region
import pandas as pd

#########################################################
#                                                       #
#                      CONSTANTS                        #
#                                                       #
#########################################################

PS = 0.3 # PLAYER_SIZE
PB = 0.085 # PLAYER_BODY
CPD = PS+PB # CERTAIN POSSESSION DISTANCE
KR = 0.7 # KICKABLE RADIUS
KA = (PS + PB + KR)*1.05 # KICKABLE AREA
DD = 1.2*2*1.05 # DASHABLE DISTANCE
PMS = 1.2*1.05 # PLAYER MAXIMUM SPEED
RS = (2*KA)/1.5 # REACTION SPEED

#########################################################
#                                                       #
#                        MODEL                          #
#                                                       #
#########################################################
#create fuzzy input regions
## input 1: distance from player to ball
dist_minor = Region('D1', 1000, 0, 100, Trapezoid(0, 1.5*CPD, 0, CPD).function)
dist_fair = Region('D2', 1000, 0, 100, Triangular(CPD, 1.5*KA, KA).function)
dist_great = Region('D3', 1000, 0, 100, Trapezoid(KA, 100, DD, 100).function)
distance = [dist_minor, dist_fair, dist_great]

## input 2: relative speed from ball to player
rspeed_minor = Region('RS1', 50, 0, 5, Trapezoid(0, 1.5*RS, 0, RS).function)
rspeed_great = Region('RS2', 50, 0, 5, Trapezoid(RS, 5, 1.5*RS, 5).function)
relative_speed = [rspeed_minor, rspeed_great]

## input 3: ball absolute speed
bspeed_minor = Region('BS1', 100, 0, 10, Trapezoid(0, 1.5*PMS, 0, PMS).function)
bspeed_great = Region('BS2', 100, 0, 10, Trapezoid(PMS, 10, PMS, 10).function)
ball_speed = [bspeed_minor, bspeed_minor]

# output
## ball possession
bposs_false = Region('BPF', 10, 0, 1, Triangular(0, 0.75).function)
bposs_true = Region('BPT', 10, 0, 1, Triangular(0.5, 1).function)
ball_possession = [bposs_false, bposs_true]

#########################################################
#                                                       #
#                        RULES                          #
#                                                       #
#########################################################
def rules(dist, rspeed, bspeed):
    if dist == dist_minor and rspeed == rspeed_minor and bspeed == bspeed_minor: return bposs_true
    if dist == dist_minor and rspeed == rspeed_minor and bspeed == bspeed_great: return bposs_true
    if dist == dist_minor and rspeed == rspeed_great and bspeed == bspeed_minor: return bposs_true
    if dist == dist_minor and rspeed == rspeed_great and bspeed == bspeed_great: return bposs_true
    if dist == dist_fair  and rspeed == rspeed_minor and bspeed == bspeed_minor: return bposs_true
    if dist == dist_fair  and rspeed == rspeed_minor and bspeed == bspeed_great: return bposs_true
    if dist == dist_fair  and rspeed == rspeed_great and bspeed == bspeed_minor: return bposs_true
    if dist == dist_fair  and rspeed == rspeed_great and bspeed == bspeed_great: return bposs_false
    if dist == dist_great and rspeed == rspeed_minor and bspeed == bspeed_minor: return bposs_false
    if dist == dist_great and rspeed == rspeed_minor and bspeed == bspeed_great: return bposs_false
    if dist == dist_great and rspeed == rspeed_great and bspeed == bspeed_minor: return bposs_false
    if dist == dist_great and rspeed == rspeed_great and bspeed == bspeed_great: return bposs_false


#create reader with default data path values
reader = Reader()

#while there's a file to read run application
status = True
while status:
    status, distance, relative_speed, ball_speed = reader.read_next_file()