import matplotlib.pyplot as plt


def plot_function(function, init=0, end=10):
    axis_x = []
    axis_y = []
    for x in range(init * 10, (end + 1) * 10):
        x = x / 10
        axis_x.append(x)
        axis_y.append(function(x))
    plt.plot(axis_x, axis_y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Plotted Function')
    plt.show(block=False)
    plt.pause(1)
    plt.close()
