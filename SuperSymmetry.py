import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import stats
import numpy as np
from scipy import sparse


class SuperSymmetry:
    scale_up_value = 100
    run_env = 'bhaduri'
    base_dir = '/home/'+run_env+'/MEGA/supersymmetry/'
    file_ext = '.csv'

    def __init__(self):
        print("Start SS")

    def reorder_Px_Py_Pz(self, raw_file, file_subject, delim_char):
        out_files = []
        rawdf = pd.read_csv(raw_file, delimiter=delim_char)
        cols = ['Px', 'Py', 'Pz']
        momentum_df = rawdf[cols]
        out_file_name = self.base_dir + file_subject + 'xy_z.csv'
        momentum_df.to_csv(out_file_name, header=False, index=None)
        out_files.append(out_file_name)
        # print('xy_z')
        # testdf = pd.read_csv(out_file_name, header=None, names=['Px', 'Py', 'Pz'])
        # print(testdf.head())

        cols = ['Py', 'Pz', 'Px']
        momentum_df = rawdf[cols]
        out_file_name = self.base_dir + file_subject + 'yz_x.csv'
        momentum_df.to_csv(out_file_name, header=False, index=None)
        out_files.append(out_file_name)

        cols = ['Px', 'Pz', 'Py']
        momentum_df = rawdf[cols]
        out_file_name = self.base_dir + file_subject + 'xz_y.csv'
        momentum_df.to_csv(out_file_name, header=False, index=None)
        out_files.append(out_file_name)
        print(out_files)
        return out_files

    def read_raw_and_write_dimoun_momentums(self, momentum_in_file):
        momentum_Px_Py_Pz = pd.read_csv(momentum_in_file, header=None, names=['Px', 'Py', 'Pz'])

        # Get only momentum columns
        # momentum_Px_Py_Pz = rawdf[['Px', 'Py', 'Pz']]
        print(momentum_Px_Py_Pz.head())
        # remove outliers
        momentum_Px_Py_Pz = momentum_Px_Py_Pz[(np.abs(stats.zscore(momentum_Px_Py_Pz)) < 3).all(axis=1)]
        # move to positive quadrant
        momentum_Px_Py_Pz = momentum_Px_Py_Pz - momentum_Px_Py_Pz.min()

        # scale up Px and Py for matrix formation of x - y plane
        momentum_Px_Py_Pz['Px'] = momentum_Px_Py_Pz['Px'] * self.scale_up_value
        momentum_Px_Py_Pz['Py'] = momentum_Px_Py_Pz['Py'] * self.scale_up_value
        momentum_Px_Py_Pz['Pz'] = momentum_Px_Py_Pz['Pz']

        # convert to integer x y values
        cols = ['Px', 'Py']
        for col in cols:
            momentum_Px_Py_Pz[col] = momentum_Px_Py_Pz[col].apply(lambda x: int(x))
        # print(momentum_Px_Py_Pz.head())
        # print(momentum_Px_Py_Pz.shape)
        momentum_Px_Py_Pz = momentum_Px_Py_Pz.sort_values(['Px', 'Py']).drop_duplicates(['Px', 'Py']).reset_index(drop=True)
        print(momentum_Px_Py_Pz.shape)
        print(momentum_Px_Py_Pz.max())
        momentum_in_file_parts = momentum_in_file.split('.')
        momentum_out_file = momentum_in_file_parts[0]+'_out.csv'
        print('Output written to :', momentum_out_file)
        momentum_Px_Py_Pz.to_csv(momentum_out_file, index=None, header=False)

    def read_raw_and_write_SS_momentums(self, ss_raw_file, delim):
        rawdf = pd.read_csv(ss_raw_file, delimiter=delim)
        # Get only momentum columns
        momentum_Px_Py_Pz = rawdf[['Px', 'Py', 'Pz']]

        # remove outliers
        momentum_Px_Py_Pz = momentum_Px_Py_Pz[(np.abs(stats.zscore(momentum_Px_Py_Pz)) < 3).all(axis=1)]
        # move to positive quadrant
        momentum_Px_Py_Pz = momentum_Px_Py_Pz - momentum_Px_Py_Pz.min()
        print(momentum_Px_Py_Pz.max())
        # scale up Px and Py for matrix formation of x - y plane
        momentum_Px_Py_Pz['Px'] = momentum_Px_Py_Pz['Px'] * self.scale_up_value
        momentum_Px_Py_Pz['Py'] = momentum_Px_Py_Pz['Py'] * self.scale_up_value

        # convert to integer x y values
        cols = ['Px', 'Py']
        for col in cols:
            momentum_Px_Py_Pz[col] = momentum_Px_Py_Pz[col].apply(lambda x: int(x))
        print(momentum_Px_Py_Pz.head())
        print(momentum_Px_Py_Pz.shape)
        momentum_Px_Py_Pz = momentum_Px_Py_Pz.sort_values(['Px', 'Py']).drop_duplicates(['Px', 'Py']).reset_index(drop=True)
        print(momentum_Px_Py_Pz.shape)
        print(momentum_Px_Py_Pz.max())
        momentum_Px_Py_Pz.to_csv('/home/dgrfi/MEGA/supersymmetry/SS100.csv', index=None, header=False)

    def plt_3d_momentum(self, momentum_Px_Py_Pz):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        Px_value = momentum_Px_Py_Pz['X']
        Py_value = momentum_Px_Py_Pz['Y']
        Pz_value = momentum_Px_Py_Pz['Z']
        ax.scatter3D(Px_value, Py_value, Pz_value)
        plt.show()
