import pandas as pd
import matplotlib.pyplot as plt

class Muonml :
    def __init__(self):
        print("ML")

    def read_muon_data(self):
        column_names = ['muon_eta_1', 'muon_eta_2', 'muon_phi_1','muon_phi_2','gheu', 'event_number', 'run_number', 'luminocity']
        muondata8 = pd.read_csv('/home/dgrfi/MEGA/dimuon/data/ephimassdi8.txt', delimiter=';', header=None, names=column_names)

        print(muondata8.head())
