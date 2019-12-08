from ball_possession.fuzzy.region import Region
from ball_possession.functions.triangular import Triangular
from ball_possession.graphics.plot_region import plot_region

# test all default
triangular = Triangular(150, 175)
region = Region('default region', 1000, 100, 200, triangular.function)
plot_region(region, 'testing ' + region.name)

# test name
region.name = 'region with changed name'
plot_region(region, 'testing ' + region.name)

# test npoints
region.npoints = 50
region.name = 'region with low npoints'
plot_region(region, 'testing ' + region.name)
region.npoints = 100000
region.name = 'region with high npoints'
plot_region(region, 'testing ' + region.name)
region.npoints = 1000

# test init
region.init = -100
region.name = 'region with low init'
plot_region(region, 'testing ' + region.name)
region.init = 160
region.name = 'region with slightly high init'
plot_region(region, 'testing ' + region.name)
region.init = 190
region.name = 'region with high init'
plot_region(region, 'testing ' + region.name)
region.init = 100

# test end
region.end = 101
region.name = 'region with low end'
plot_region(region, 'testing ' + region.name)
region.end = 160
region.name = 'region with slightly low end'
plot_region(region, 'testing ' + region.name)
region.end = 500
region.name = 'region with high end'
plot_region(region, 'testing ' + region.name)
region.end = 200