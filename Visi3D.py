import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Visi3D:

    def __init__(self):
        print('3dplot')
    def draw_3D_Visi(self):
        # momentum_Px_Py_Pz = pd.read_csv('/home/bhaduri/Documents/3D/3DVisi.csv')
        # print(momentum_Px_Py_Pz.head())
        self.plt_3d_momentum()

    def plt_3d_momentum(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_ylim(bottom=0)
        ax.set_ylim(top=8)
        ax.set_xlim(left=0)
        ax.set_xlim(right=10)
        ax.set_zlim(bottom=0)
        ax.set_zlim(top=5)

        x = [3,   1, 5, 6, 8]  # x coordinates of each bar
        y = [3.1, 4, 6, 2, 3.7]  # y coordinates of each bar
        items_count_x = len(x)
        items_count_y = len(y)
        items_count_z = 5
        z = np.zeros(items_count_z)  # z coordinates of each bar
        dx = np.full(items_count_x, 0.1)  # Width of each bar
        dy = np.full(items_count_y, 0.1)  # Depth of each bar
        dz = [5, 2, 3, 3, 4]  # Height of each bar
        # Pz_value = momentum_Px_Py_Pz['Z']
        # dx = [0.5, 0.5, 0.5, 0.5, 0.5]
        # dy = [0.5, 0.5, 0.5, 0.5, 0.5]
        # dz = [1, 0.5, 0.5, 0.5, 0.5]
        # print(items_count_x, items_count_y)
        ax.text(3, 3.1, 5.07, "$(X_{i+1},Y_{i+1},Z_{i+1})$")
        ax.text(0, 4, 2.07, "$(X_{i},Y_{i},Z_{i})$")
        ax.text(5, 6, 3.07, "$(X_{i+2},Y_{i+2},Z_{i+2})$")
        ax.text(5, 2, 3.5, "$(X_{i+3},Y_{i+3},Z_{i+3})$")
        ax.text(9.5, 2, 4.07, "$(X_{i+4},Y_{i+4},Z_{i+4})$")
        ax.bar3d(x, y, z, dx, dy, dz, color='#000000')

        # line_x = [1, 3,    5, 6, 9, 5, 3,   1, 3,   6]
        # line_y = [4, 3.1,  6, 2, 1, 6, 3.1, 4, 3.1, 2]
        # line_z = [2, 5,    3, 4, 3, 3, 5,   2, 5,   4]
        line_x = [1, 3,  1, 5, 3,   6,   8, 5, 8, 3,   6,   5, 8, 1]
        line_y = [4, 3.1,4, 6, 3.1, 2,   3.7, 6, 3.7, 3.1, 2,   6, 3.7, 4]
        line_z = [2, 5,  2, 3, 5,   3,   4, 3, 4, 5,   3, 3, 4, 2]
        line_x_ground = [6,1]
        line_y_ground = [2,4]
        line_z_ground = [0,0]
        ax.plot(line_x, line_y, line_z, color='#90949C')
        ax.plot(line_x_ground, line_y_ground, line_z_ground, color='#000000', linestyle='--')
        plt.show()
        # x = [1, 2, 3]  # x coordinates of each bar
        # y = [1, 2, 3]  # y coordinates of each bar
        # z = np.zeros(3)  # z coordinates of each bar
        # dx = [0.1, 0.1, 0.1]  # Width of each bar

        # dy = [0.1, 0.1, 0.1]  # Depth of each bar
