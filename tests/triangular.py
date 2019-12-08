from ball_possession.functions.triangular import Triangular
from ball_possession.graphics.plot_function import plot_function

#test all default
function = Triangular(5, 10)
plot_function(function.function, 0, 15)

#test center
function = Triangular(5, 10, center=5.1)
plot_function(function.function, -10, 15)
function = Triangular(5, 10, center=7)
plot_function(function.function, -10, 15)
function = Triangular(5, 10, center=9)
plot_function(function.function, -10, 15)
function = Triangular(5, 10, center=9.9)
plot_function(function.function, -10, 15)

#test peak
function = Triangular(5, 10, peak=5)
plot_function(function.function, -10, 15)
function = Triangular(5, 10, peak=0)
plot_function(function.function, -10, 15)
function = Triangular(5, 10, peak=-5)
plot_function(function.function, -10, 15)

#test floor
function = Triangular(5, 10, floor=-5)
plot_function(function.function, -10, 15)
function = Triangular(5, 10, floor=1)
plot_function(function.function, -10, 15)
function = Triangular(5, 10, floor=5)
plot_function(function.function, -10, 15)