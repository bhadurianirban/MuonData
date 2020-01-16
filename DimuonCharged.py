import pandas as pd
class DimuonCharged:

    def __init__(self):
        print('Dimuon Charged')

    def extract_dimuon_charged(self, input_file_path, tev):
        outputfile_prefix = 'dm'+tev
        orig_df = pd.read_csv(input_file_path, delimiter=';')
        orig_df_pos = orig_df[orig_df['Charge'] == 1]
        print(orig_df_pos.head())