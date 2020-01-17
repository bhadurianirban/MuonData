import pandas as pd
class DimuonCharged:

    def __init__(self):
        print('Dimuon Charged')

    def extract_dimuon_charged(self, input_file_path, tev):
        outputfile_prefix = 'dm'+tev
        orig_df = pd.read_csv(input_file_path, delimiter=';')
        df_neg = orig_df[orig_df['Charge'] == -1]
        df_pos = orig_df[orig_df['Charge'] == 1]
        df_pos_eta = df_pos['Eta']
        df_neg_eta = df_neg['Eta']
        df_pos_phi = df_pos['Phi']
        df_neg_phi = df_neg['Phi']


