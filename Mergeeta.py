import pandas as pd


class Mergeeeta:
    def __init__(self):
        print("gheu")

    def read_and_merge_eta(self):
        muondata = pd.read_csv('/home/dgrfi/MEGA/dimuon/data/ephimassdi7.txt', delimiter=';', header=None)
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
        muoneta.to_csv('/home/dgrfi/MEGA/dimuon/data/gheu.txt',index=None)

    def plot_eta(self):
        muoneta = pd.read_csv('/home/dgrfi/MEGA/dimuon/data/gheu.txt')
        muoneta.plot
