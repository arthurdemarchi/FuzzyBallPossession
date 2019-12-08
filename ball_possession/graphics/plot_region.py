import matplotlib.pyplot as plt
from ball_possession.fuzzy.region import Region


def plot_region(region,
                title,
                x_label='x',
                y_label='u(x)',
                write=False,
                file='figura.png'):

    #scatter if to plot one region
    if type(region) == Region:
        x = []
        y = []
        delta_x = region.init
        for item in region.fuzzy:
            x.append(item['x'])
            y.append(item['u'])
        plt.scatter(x, y, s=0.1, alpha=1)

    #scatter if to plot multiple regions
    elif type(region) == list:
        delta_x = region[0].init
        for each_region in region:
            x = []
            y = []
            for item in each_region.fuzzy:
                x.append(item['x'])
                y.append(item['u'])
            plt.scatter(x, y, s=0.1, alpha=1)

    #prepare plot titles and lables
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xlim(left=delta_x)
    plt.ylim(bottom=0)

    #write to disk
    if write:
        plt.savefig(file)
        plt.close()

    #show in GUI
    else:
        plt.show(block=False)
        plt.pause(3)
        plt.close()
