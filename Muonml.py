import pandas as pd
import matplotlib.pyplot as plt

class Muonml :
    def __init__(self):
        print("ML")

    def read_muon_data(self):
        # column_names = ['muon_eta_1', 'muon_eta_2', 'muon_phi_1','muon_phi_2','gheu', 'event_number', 'run_number', 'luminocity']
        vg_degree_prob = pd.read_csv('/home/bhaduri/MEGA/dimuon/results/PSVG7.csv', delimiter=',')
        vg_degree_prob_required = vg_degree_prob.iloc[5:]
        print(vg_degree_prob_required.head())
        X = vg_degree_prob_required['Log of Degree Value']
        Y = vg_degree_prob_required['Log of Probability of Degree Value']
        plt.scatter(X, Y)
        plt.show()

