import numpy as np
import matplotlib.pyplot as plot

class BumbuSin:

    def __init__(self):
        print('bumbu')

    def plot_sine(self):
        time = np.arange(0, 10, 0.1);
        print(time)
        amplitude_cos = np.tan(time)
        # amplitude_sin = np.sin(time)

        plot.plot(time, amplitude_cos)
        # plot.plot(time, amplitude_sin)
        plot.axhline(y=0, color='k')
        plot.show()