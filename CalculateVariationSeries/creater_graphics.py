import math
from matplotlib import pyplot as plt


def plot_histogram(sampling, particularity):
    x = []
    y = []
    for i in range(len(sampling)):
        x_min = sampling[i][0]
        x_max = sampling[i][1]
        rl = (x_max + x_min) / 2
        gl = particularity[i]
        x.append(rl)
        y.append(gl)
        plt.bar(rl, gl, width=2, color="b")
    plt.plot(x, y, color="r")
    plt.show()

# Хуита
def plot_polygon(sampling, accumulated_particularity):
    rl = []
    gl = []
    for i in range(len(sampling)):
        x_min = sampling[i][0]
        x_max = sampling[i][1]
        rl.append(x_max)
        gl.append(accumulated_particularity[i])
        plt.plot([x_min, x_max], [accumulated_particularity[i], accumulated_particularity[i]], color="b")
    plt.plot(rl, gl, color="r")
    plt.show()


