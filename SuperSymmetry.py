import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import stats
import numpy as np
from scipy import sparse

class SuperSymmetry:
    scale_up_value = 1000

    def __init__(self):
        print("Start SS")

    def read_raw_and_write_momentums(self):
        rawdf = pd.read_csv('/home/dgrfi/MEGA/supersymmetry/DiMu7Txyz1L.csv', delimiter=';')

        momentum_df = rawdf[['Px', 'Py', 'Pz']]

        min_px_py_pz = momentum_df.min()
        momentum_Px_Py_Pz = pd.DataFrame(columns=['Px', 'Py', 'Pz'])
        # momentum_Px_Py_Pz['Px'] = (momentum_df.loc[:, 'Px'] - min_px_py_pz['Px'])
        # momentum_Px_Py_Pz['Py'] = (momentum_df.loc[:, 'Py'] - min_px_py_pz['Py'])
        # momentum_Px_Py_Pz['Pz'] = (momentum_df.loc[:, 'Pz'] - min_px_py_pz['Pz'])
        momentum_Px_Py_Pz['Px'] = momentum_df['Px']
        momentum_Px_Py_Pz['Py'] = momentum_df['Py']
        momentum_Px_Py_Pz['Pz'] = momentum_df['Pz']
        data_count = momentum_Px_Py_Pz.shape
        minm = momentum_Px_Py_Pz.min()
        maxm = momentum_Px_Py_Pz.max()
        # print('Max ', maxm, 'Min ', minm, 'Count ', data_count)
        # fig = plt.figure()
        # ax = plt.axes(projection='3d')

        # momentum_Px_Py_Pz['Px'] = (momentum_df.loc[:, 'Px'] - min_px_py['Px']) * self.scale_up_value
        # momentum_Px_Py_Pz['Py'] = (momentum_df.loc[:, 'Py'] - min_px_py['Py']) * self.scale_up_value
        # momentum_Px_Py_Pz['Pz'] = (momentum_df.loc[:, 'Pz'] - min_px_py['Pz']) * self.scale_up_value
        # print(momentum_Px_Py_Pz.head())
        # cols = ['Px', 'Py', 'Pz']
        # for col in cols:
        #     momentum_Px_Py_Pz[col] = momentum_Px_Py_Pz[col].apply(lambda x: int(x))
        # plt.scatter(Px_value, Py_value)
        # plt.show()
        # Px_value = momentum_Px_Py_Pz['Px']
        # Py_value = momentum_Px_Py_Pz['Py']
        # Pz_value = momentum_Px_Py_Pz['Pz']
        # ax.scatter3D(Px_value, Py_value, Pz_value)
        # plt.show()

        momentum_Px_Py_Pz = momentum_Px_Py_Pz[(np.abs(stats.zscore(momentum_df)) < 3).all(axis=1)]

        momentum_Px_Py_Pz = momentum_Px_Py_Pz * self.scale_up_value

        cols = ['Px', 'Py', 'Pz']
        for col in cols:
            momentum_Px_Py_Pz[col] = momentum_Px_Py_Pz[col].apply(lambda x: int(x))
        minm = momentum_Px_Py_Pz.min()
        maxm = momentum_Px_Py_Pz.max()
        momentum_Px_Py_Pz['Px'] = (momentum_Px_Py_Pz.loc[:, 'Px'] - minm['Px'])
        momentum_Px_Py_Pz['Py'] = (momentum_Px_Py_Pz.loc[:, 'Py'] - minm['Py'])
        momentum_Px_Py_Pz['Pz'] = (momentum_Px_Py_Pz.loc[:, 'Pz'] - minm['Pz'])
        data_count = momentum_Px_Py_Pz.shape
        # print(data_count)
        momentum_Px_Py_Pz = momentum_Px_Py_Pz.sort_values(['Px', 'Py']).drop_duplicates().reset_index(drop=True)
        minm = momentum_Px_Py_Pz.min()
        maxm = momentum_Px_Py_Pz.max()
        data_count = momentum_Px_Py_Pz.shape
        # print('Max ', maxm, 'Min ', minm, 'Count ', data_count)
        matrix_col_count = maxm['Py']
        matrix_row_count = maxm['Px']
        row_co = momentum_Px_Py_Pz['Px']
        col_co = momentum_Px_Py_Pz['Py']
        co_value = momentum_Px_Py_Pz['Pz']

        mat_coo = sparse.coo_matrix((co_value, (row_co, col_co)))
        print(mat_coo)
        sdf = pd.DataFrame.sparse.from_spmatrix(mat_coo)
        # sdf = pd.SparseDataFrame(mat_coo)
        # sdf.sparse.to_dense()
        print(sdf[27628, 17391])

        # momentum_dense = pd.DataFrame(mat_coo.todense())
        # print(momentum_dense)
        # fig = plt.figure()
        # ax = plt.axes(projection='3d')
        # ax.scatter3D(Px_value, Py_value, Pz_value)
        # plt.show()
