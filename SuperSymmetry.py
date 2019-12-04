import  pandas as pd


class SuperSymmetry:
    scale_up_value = 10000

    def __init__(self):
        print("Start SS")

    def read_raw_and_write_momentums(self):
        rawdf = pd.read_csv('/home/bhaduri/MEGA/supersymmetry/DiMu7Txyz1L.csv', delimiter=';')

        momentum_df = rawdf[['Px', 'Py', 'Pz']]
        min_px_py = momentum_df.min()

        momentum_Px_Py_Pz = pd.DataFrame(columns=['Px', 'Py', 'Pz'])
        momentum_Px_Py_Pz['Px'] = (momentum_df.loc[:, 'Px'] - min_px_py['Px']) * self.scale_up_value
        momentum_Px_Py_Pz['Py'] = (momentum_df.loc[:, 'Py'] - min_px_py['Py']) * self.scale_up_value
        momentum_Px_Py_Pz['Pz'] = (momentum_df.loc[:, 'Pz'] - min_px_py['Pz']) * self.scale_up_value
        print(momentum_Px_Py_Pz.head())
