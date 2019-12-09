from ball_possession.functions.trapezoid import Trapezoid
from ball_possession.graphics.plot_function import plot_function

#test all default
function = Trapezoid(5, 25, 10, 20)
plot_function(function.function, 0, 50)

#test peak_init
function = Trapezoid(-15, 25, -15, 20)
plot_function(function.function, -20, 30)
function = Trapezoid(-15, 25, 0, 20)
plot_function(function.function, -20, 30)
function = Trapezoid(-15, 25, 15, 20)
plot_function(function.function, -20, 30)
function = Trapezoid(-15, 25, 20, 20)
plot_function(function.function, -20, 30)

#test peak_end
function = Trapezoid(-15, 20, -10, -10)
plot_function(function.function, -20, 30)
function = Trapezoid(-15, 20, -10, -5)
plot_function(function.function, -20, 30)
function = Trapezoid(-15, 20, -10, 0)
plot_function(function.function, -20, 30)
function = Trapezoid(-15, 20, -10, 20)
plot_function(function.function, -20, 30)

#test peak
function = Trapezoid(5, 25, 10, 20, peak=5)
plot_function(function.function, -10, 30)
function = Trapezoid(5, 25, 10, 20, peak=0)
plot_function(function.function, -10, 30)
function = Trapezoid(5, 25, 10, 20, peak=-5)
plot_function(function.function, -10, 30)

#test floor
function = Trapezoid(5, 25, 10, 20, floor=-5)
plot_function(function.function, -10, 30)
function = Trapezoid(5, 25, 10, 20, floor=1)
plot_function(function.function, -10, 30)
function = Trapezoid(5, 25, 10, 20, floor=5)
plot_function(function.function, -10, 30)