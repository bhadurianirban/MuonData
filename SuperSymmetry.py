import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

class SuperSymmetry:
    scale_up_value = 10000

    def __init__(self):
        print("Start SS")

    def read_raw_and_write_momentums(self):
        rawdf = pd.read_csv('/home/bhaduri/MEGA/supersymmetry/DiMu7Txyz1L.csv', delimiter=';')

        momentum_df = rawdf[['Px', 'Py', 'Pz']]
        min_px_py = momentum_df.min()

        # momentum_Px_Py_Pz = pd.DataFrame(columns=['Px', 'Py', 'Pz'])

        Px_value = momentum_df['Px']
        Py_value = momentum_df['Py']
        # plt.scatter(Px_value, Py_value)
        # plt.show()

        momentum_df = momentum_df[(np.abs(stats.zscore(momentum_df)) < 3).all(axis=1)]
        Px_value = momentum_df['Px']
        Py_value = momentum_df['Py']
        plt.scatter(Px_value, Py_value)
        plt.show()
        # momentum_Px_Py_Pz['Px'] = (momentum_df.loc[:, 'Px'] - min_px_py['Px']) * self.scale_up_value
        # momentum_Px_Py_Pz['Py'] = (momentum_df.loc[:, 'Py'] - min_px_py['Py']) * self.scale_up_value
        # momentum_Px_Py_Pz['Pz'] = (momentum_df.loc[:, 'Pz'] - min_px_py['Pz']) * self.scale_up_value
        # print(momentum_Px_Py_Pz.head())
