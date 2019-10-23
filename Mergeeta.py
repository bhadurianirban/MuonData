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
        muoneta.to_csv('/home/dgrfi/MEGA/dimuon/data/gheu8.txt', index=None)

    def read_and_merge_phi(self):
        muondata = pd.read_csv('/home/dgrfi/MEGA/dimuon/data/ephimassdi7.txt', delimiter=';', header=None)
        # print (muondata)

        # muondata.to_csv('/home/dgrfi/MEGA/dimuon/data/gheu.txt', header=None, columns=[0], index=None)
        muonetaphi = pd.DataFrame(columns=['eta', 'phi'])
        rowcount = 0
        for row in muondata.itertuples():
            # print(row[0], row[1], row[2], row[3], row[4])
            muonetaphi.loc[rowcount, 'eta'] = row[1]
            muonetaphi.loc[rowcount, 'phi'] = row[3]
            rowcount = rowcount + 1
            muonetaphi.loc[rowcount, 'eta'] = row[2]
            muonetaphi.loc[rowcount, 'phi'] = row[4]
            # print(muonetaphi['phi'].loc[rowcount])
            rowcount = rowcount + 1

        # print(muonetaphi)
        muonetaphi.to_csv('/home/dgrfi/MEGA/dimuon/data/phi7H.csv', index=None)

    def save_phi_for_corr_eta(self):
        muonetaphi7 = pd.read_csv('/home/bhaduri/MEGA/dimuon/data/phi7H.csv')
        muonetaphi8 = pd.read_csv('/home/bhaduri/MEGA/dimuon/data/phi8H.csv')
        muonetaphi7['phi'].to_csv('/home/bhaduri/MEGA/dimuon/data/phi7.csv', index=None, header=False)
        muonetaphi8['phi'].to_csv('/home/bhaduri/MEGA/dimuon/data/phi8.csv', index=None, header=False)

    def plot_eta(self):
        muoneta = pd.read_csv('/home/bhaduri/MEGA/dimuon/data/gheu.txt')
        print(muoneta)
        # muonetawithindex = muoneta.reset_index()
        muoneta.hist(bins=20)
        plt.title('7TEV 20 bins')
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

    def divide_eta(self):
        eta7tev = pd.read_csv('/home/bhaduri/MEGA/dimuon/data/eta7H.csv')
        eta8tev = pd.read_csv('/home/bhaduri/MEGA/dimuon/data/eta8H.csv')
        # eta7tev['gheu'] = pd.qcut(eta7tev['eta'], q=5, labels=['a', 'b', 'c', 'd', 'e'])
        eta_labels = ['a', 'b', 'c', 'd', 'e']
        print(pd.cut(eta7tev['eta'], bins=5, precision=5))
        eta7tev['partitions'] = pd.cut(eta7tev['eta'], bins=5, precision=5, labels=eta_labels)
        for label in eta_labels:
            eta7tev[(eta7tev['partitions'] == label)]['eta'].to_csv(
                '/home/bhaduri/MEGA/dimuon/data/eta7part/eta7' + label + '.csv',
                index=None, header=False)

        print(pd.cut(eta8tev['eta'], bins=5, precision=5))
        eta8tev['partitions'] = pd.cut(eta8tev['eta'], bins=5, precision=5, labels=eta_labels)
        for label in eta_labels:
            eta8tev[(eta8tev['partitions'] == label)]['eta'].to_csv(
                '/home/bhaduri/MEGA/dimuon/data/eta8part/eta8' + label + '.csv',
                index=None, header=False)

    def divide_phi(self):
        phi7tev = pd.read_csv('/home/bhaduri/MEGA/dimuon/data/phi7H.csv')
        phi8tev = pd.read_csv('/home/bhaduri/MEGA/dimuon/data/phi8H.csv')
        # eta7tev['gheu'] = pd.qcut(eta7tev['eta'], q=5, labels=['a', 'b', 'c', 'd', 'e'])
        phi_labels = ['a', 'b', 'c', 'd', 'e']
        print(pd.cut(phi7tev['eta'], bins=5, precision=5))
        phi7tev['partitions'] = pd.cut(phi7tev['eta'], bins=5, precision=5, labels=phi_labels)
        for label in phi_labels:
            phi7tev[(phi7tev['partitions'] == label)]['phi'].to_csv(
                '/home/bhaduri/MEGA/dimuon/data/phi7part/phi7' + label + '.csv',
                index=None, header=False)

        print(pd.cut(phi8tev['eta'], bins=5, precision=5))
        phi8tev['partitions'] = pd.cut(phi8tev['eta'], bins=5, precision=5, labels=phi_labels)
        for label in phi_labels:
            phi8tev[(phi8tev['partitions'] == label)]['phi'].to_csv(
                '/home/bhaduri/MEGA/dimuon/data/phi8part/phi8' + label + '.csv',
                index=None, header=False)
