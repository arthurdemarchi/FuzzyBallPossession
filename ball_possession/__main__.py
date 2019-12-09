from .input_reader.reader import Reader
from .functions.triangular import Triangular
from .functions.trapezoid import Trapezoid
from .fuzzy.region import Region
from .graphics.plot_region import plot_region
from .fuzzy.operators import inference, defuzzyficate, classificate

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
dist_great = Region('D3', 10000, 0, 100, Trapezoid(KA, 100, DD, 100).function)
distance = [dist_minor, dist_fair, dist_great]
plot_region(distance, 'Distância do Jogador à Bola', write=True, file='figures/input1.png')

## input 2: relative speed from ball to player
rspeed_minor = Region('RS1', 500, 0, 5, Trapezoid(0, 1.5*RS, 0, RS).function)
rspeed_great = Region('RS2', 500, 0, 5, Trapezoid(RS, 5, 1.5*RS, 5).function)
relative_speed = [rspeed_minor, rspeed_great]
plot_region(relative_speed, 'Velocidade Relativa do Jogador à Bola', write=True, file='figures/input2.png')

## input 3: ball absolute speed
bspeed_minor = Region('BS1', 1000, 0, 10, Trapezoid(0, 1.5*PMS, 0, PMS).function)
bspeed_great = Region('BS2', 1000, 0, 10, Trapezoid(PMS, 10, 1.5*PMS, 10).function)
ball_speed = [bspeed_minor, bspeed_great]
plot_region(ball_speed, 'Velocidade Absoluta da Bola', write=True, file='figures/input3.png')

# output
## ball possession
bposs_false = Region('False', 1000, 0, 1, Triangular(0, 0.75).function)
bposs_true = Region('True', 1000, 0, 1, Triangular(0.5, 1).function)
ball_possession = [bposs_false, bposs_true]
plot_region(ball_speed, 'Posse de Bola', write=True, file='figures/output.png')

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

#########################################################
#                                                       #
#                      OPERATION                        #
#                                                       #
#########################################################
#create reader with default data path values
reader = Reader()

#while there's a file to read run application
possessions = []
status = True
while status:
    status, distance_values, relative_speed_values, ball_speed_values = reader.read_next_file()
    for i in range(len(distance_values)):
        fuzzy = inference([distance, relative_speed, ball_speed], [distance_values[i], relative_speed_values[i], ball_speed_values[i]], rules, 'mandani', 'max')
        value = defuzzyficate(fuzzy, 'cda')
        classification = classificate(ball_possession, value)
        possessions.append(classification)
        print('    ', i, 'of ', len(distance_values))
    reader.write_output(possessions)