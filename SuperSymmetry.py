import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import stats
import numpy as np

class SuperSymmetry:
    scale_up_value = 10000

    def __init__(self):
        print("Start SS")

    def read_raw_and_write_momentums(self):
        rawdf = pd.read_csv('/home/dgrfi/MEGA/supersymmetry/DiMu7Txyz1L.csv', delimiter=';')

        momentum_df = rawdf[['Px', 'Py', 'Pz']]
        min_px_py_pz = momentum_df.min()
        momentum_Px_Py_Pz = pd.DataFrame(columns=['Px', 'Py', 'Pz'])
        momentum_Px_Py_Pz['Px'] = (momentum_df.loc[:, 'Px'] - min_px_py_pz['Px'])
        momentum_Px_Py_Pz['Py'] = (momentum_df.loc[:, 'Py'] - min_px_py_pz['Py'])
        momentum_Px_Py_Pz['Pz'] = (momentum_df.loc[:, 'Pz'] - min_px_py_pz['Pz'])

        # momentum_Px_Py_Pz['Px'] = (momentum_df.loc[:, 'Px'] - min_px_py['Px']) * self.scale_up_value
        # momentum_Px_Py_Pz['Py'] = (momentum_df.loc[:, 'Py'] - min_px_py['Py']) * self.scale_up_value
        # momentum_Px_Py_Pz['Pz'] = (momentum_df.loc[:, 'Pz'] - min_px_py['Pz']) * self.scale_up_value
        # print(momentum_Px_Py_Pz.head())
        # cols = ['Px', 'Py', 'Pz']
        # for col in cols:
        #     momentum_Px_Py_Pz[col] = momentum_Px_Py_Pz[col].apply(lambda x: int(x))
        minm = momentum_Px_Py_Pz.min()
        maxm = momentum_Px_Py_Pz.max()
        print(maxm, minm)
        # plt.scatter(Px_value, Py_value)
        # plt.show()
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        # Px_value = momentum_Px_Py_Pz['Px']
        # Py_value = momentum_Px_Py_Pz['Py']
        # Pz_value = momentum_Px_Py_Pz['Pz']
        # ax.scatter3D(Px_value, Py_value, Pz_value)
        # plt.show()

        momentum_Px_Py_Pz = momentum_Px_Py_Pz[(np.abs(stats.zscore(momentum_df)) < 3).all(axis=1)]
        Px_value = momentum_Px_Py_Pz['Px']
        Py_value = momentum_Px_Py_Pz['Py']
        Pz_value = momentum_Px_Py_Pz['Pz']
        ax.scatter3D(Px_value, Py_value, Pz_value, c=Pz_value, cmap='Greens')
        plt.show()