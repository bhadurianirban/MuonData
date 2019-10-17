import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Mergeeeta:
    def __init__(self):
        print("gheu")

    def read_and_merge_eta(self):
        muondata = pd.read_csv('/home/dgrfi/MEGA/dimuon/data/ephimassdi8.txt', delimiter=';', header=None)
        # print (muondata)

        # muondata.to_csv('/home/dgrfi/MEGA/dimuon/data/gheu.txt', header=None, columns=[0], index=None)
        muoneta = pd.DataFrame(columns=['eta'])
        rowcount = 0
        for row in muondata.itertuples():
            # print(row[0], row[1], row[2])
            muoneta.loc[rowcount] = row[1]
            rowcount = rowcount + 1
            muoneta.loc[rowcount] = row[2]
            rowcount = rowcount + 1
        muoneta.to_csv('/home/dgrfi/MEGA/dimuon/data/gheu8.txt',index=None)

    def plot_eta(self):
        muoneta = pd.read_csv('/home/dgrfi/MEGA/dimuon/data/gheu8.txt')
        print(muoneta)
        # muonetawithindex = muoneta.reset_index()
        muoneta.hist(bins=20)
        plt.show()
        # muoneta.reset_index().plot(kind='scatter', x='index', y='eta')
        # plt.show()
        # muoneta.plot(x=muoneta.index, y='eta', kind='scatter')
        # plt.xticks(muoneta['eta'], muoneta.index.values)  # location, labels
        # plt.plot(muoneta['eta'], type='scatter')
        # plt.show()
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('y-axis')
        # plt.xlabel('x-axis')
        # plt.show()


