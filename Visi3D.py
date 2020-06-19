import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Visi3D:

    def __init__(self):
        print('3dplot')
    def draw_3D_Visi(self):
        momentum_Px_Py_Pz = pd.read_csv('/home/bhaduri/Documents/3D/3DVisi.csv')
        print(momentum_Px_Py_Pz.head())
        self.plt_3d_momentum(momentum_Px_Py_Pz)

    def plt_3d_momentum(self, momentum_Px_Py_Pz):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        x = momentum_Px_Py_Pz['X']  # x coordinates of each bar
        y = momentum_Px_Py_Pz['Y']  # y coordinates of each bar
        items_count_x = len(x)
        items_count_y = len(y)
        items_count_z = len(momentum_Px_Py_Pz['Z'])
        z = np.zeros(items_count_z)  # z coordinates of each bar
        dx = np.full(items_count_x, 0.1)  # Width of each bar
        dy = np.full(items_count_y, 0.1)  # Depth of each bar
        dz = momentum_Px_Py_Pz['Z']  # Height of each bar
        # Pz_value = momentum_Px_Py_Pz['Z']
        # dx = [0.5, 0.5, 0.5, 0.5, 0.5]
        # dy = [0.5, 0.5, 0.5, 0.5, 0.5]
        # dz = [1, 0.5, 0.5, 0.5, 0.5]
        print(items_count_x, items_count_y)
        ax.bar3d(x, y, z, dx, dy, dz)
        line_x = momentum_Px_Py_Pz['X']
        line_y = momentum_Px_Py_Pz['Y']
        line_z = momentum_Px_Py_Pz['Z']
        ax.plot(line_x,line_y,line_z,color='red')
        plt.show()
        # x = [1, 2, 3]  # x coordinates of each bar
        # y = [1, 2, 3]  # y coordinates of each bar
        # z = np.zeros(3)  # z coordinates of each bar
        # dx = [0.1, 0.1, 0.1]  # Width of each bar

        # dy = [0.1, 0.1, 0.1]  # Depth of each bar
