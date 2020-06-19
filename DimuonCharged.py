import pandas as pd
import os

class DimuonCharged:

    def __init__(self):
        print('Dimuon Charged')

    def extract_dimuon_charged(self, input_file_path, tev):
        outputfile_prefix = 'dm'+tev
        orig_df = pd.read_csv(input_file_path, delimiter=',')
        df_neg = orig_df[orig_df['Charge'] == -1]
        df_pos = orig_df[orig_df['Charge'] == 1]
        df_pos_eta = df_pos['Eta']
        df_neg_eta = df_neg['Eta']
        df_pos_phi = df_pos['Phi']
        df_neg_phi = df_neg['Phi']

        df_pos_sorted_by_phi = df_pos.sort_values(['Phi'])
        df_pos_eta_sorted_by_phi = df_pos_sorted_by_phi['Eta']
        df_pos_phi_sorted_by_phi = df_pos_sorted_by_phi['Phi']

        df_neg_sorted_by_phi = df_neg.sort_values(['Phi'])
        df_neg_eta_sorted_by_phi = df_neg_sorted_by_phi['Eta']
        df_neg_phi_sorted_by_phi = df_neg_sorted_by_phi['Phi']

        df_pos_a = df_pos[(df_pos['Eta'] >= -2.5) & (df_pos['Eta'] < -1.5)]
        df_pos_b = df_pos[(df_pos['Eta'] >= -1.5) & (df_pos['Eta'] < -0.5)]
        df_pos_c = df_pos[(df_pos['Eta'] >= -0.5) & (df_pos['Eta'] < 0.5)]
        df_pos_d = df_pos[(df_pos['Eta'] >= 0.5) & (df_pos['Eta'] < 1.5)]
        df_pos_e = df_pos[(df_pos['Eta'] >= 1.5) & (df_pos['Eta'] < 2.5)]

        df_neg_a = df_neg[(df_neg['Eta'] >= -2.5) & (df_neg['Eta'] < -1.5)]
        df_neg_b = df_neg[(df_neg['Eta'] >= -1.5) & (df_neg['Eta'] < -0.5)]
        df_neg_c = df_neg[(df_neg['Eta'] >= -0.5) & (df_neg['Eta'] < 0.5)]
        df_neg_d = df_neg[(df_neg['Eta'] >= 0.5) & (df_neg['Eta'] < 1.5)]
        df_neg_e = df_neg[(df_neg['Eta'] >= 1.5) & (df_neg['Eta'] < 2.5)]

        df_pos_eta_a = df_pos_a['Eta']
        df_pos_eta_b = df_pos_b['Eta']
        df_pos_eta_c = df_pos_c['Eta']
        df_pos_eta_d = df_pos_d['Eta']
        df_pos_eta_e = df_pos_e['Eta']

        df_pos_phi_a = df_pos_a['Phi']
        df_pos_phi_b = df_pos_b['Phi']
        df_pos_phi_c = df_pos_c['Phi']
        df_pos_phi_d = df_pos_d['Phi']
        df_pos_phi_e = df_pos_e['Phi']

        df_neg_eta_a = df_neg_a['Eta']
        df_neg_eta_b = df_neg_b['Eta']
        df_neg_eta_c = df_neg_c['Eta']
        df_neg_eta_d = df_neg_d['Eta']
        df_neg_eta_e = df_neg_e['Eta']

        df_neg_phi_a = df_neg_a['Phi']
        df_neg_phi_b = df_neg_b['Phi']
        df_neg_phi_c = df_neg_c['Phi']
        df_neg_phi_d = df_neg_d['Phi']
        df_neg_phi_e = df_neg_e['Phi']

        df_pos_sorted_by_phi_a = df_pos_a.sort_values(['Phi'])
        df_pos_sorted_by_phi_b = df_pos_b.sort_values(['Phi'])
        df_pos_sorted_by_phi_c = df_pos_c.sort_values(['Phi'])
        df_pos_sorted_by_phi_d = df_pos_d.sort_values(['Phi'])
        df_pos_sorted_by_phi_e = df_pos_e.sort_values(['Phi'])

        df_neg_sorted_by_phi_a = df_neg_a.sort_values(['Phi'])
        df_neg_sorted_by_phi_b = df_neg_b.sort_values(['Phi'])
        df_neg_sorted_by_phi_c = df_neg_c.sort_values(['Phi'])
        df_neg_sorted_by_phi_d = df_neg_d.sort_values(['Phi'])
        df_neg_sorted_by_phi_e = df_neg_e.sort_values(['Phi'])

        df_pos_eta_sorted_by_phi_a = df_pos_sorted_by_phi_a['Eta']
        df_pos_eta_sorted_by_phi_b = df_pos_sorted_by_phi_b['Eta']
        df_pos_eta_sorted_by_phi_c = df_pos_sorted_by_phi_c['Eta']
        df_pos_eta_sorted_by_phi_d = df_pos_sorted_by_phi_d['Eta']
        df_pos_eta_sorted_by_phi_e = df_pos_sorted_by_phi_e['Eta']

        df_neg_eta_sorted_by_phi_a = df_neg_sorted_by_phi_a['Eta']
        df_neg_eta_sorted_by_phi_b = df_neg_sorted_by_phi_b['Eta']
        df_neg_eta_sorted_by_phi_c = df_neg_sorted_by_phi_c['Eta']
        df_neg_eta_sorted_by_phi_d = df_neg_sorted_by_phi_d['Eta']
        df_neg_eta_sorted_by_phi_e = df_neg_sorted_by_phi_e['Eta']

        df_pos_phi_sorted_by_phi_a = df_pos_sorted_by_phi_a['Phi']
        df_pos_phi_sorted_by_phi_b = df_pos_sorted_by_phi_b['Phi']
        df_pos_phi_sorted_by_phi_c = df_pos_sorted_by_phi_c['Phi']
        df_pos_phi_sorted_by_phi_d = df_pos_sorted_by_phi_d['Phi']
        df_pos_phi_sorted_by_phi_e = df_pos_sorted_by_phi_e['Phi']

        df_neg_phi_sorted_by_phi_a = df_neg_sorted_by_phi_a['Phi']
        df_neg_phi_sorted_by_phi_b = df_neg_sorted_by_phi_b['Phi']
        df_neg_phi_sorted_by_phi_c = df_neg_sorted_by_phi_c['Phi']
        df_neg_phi_sorted_by_phi_d = df_neg_sorted_by_phi_d['Phi']
        df_neg_phi_sorted_by_phi_e = df_neg_sorted_by_phi_e['Phi']

        self.write_df(df_pos_eta, input_file_path, tev, 'eta', 'pos', 'full', 'unsorted')
        self.write_df(df_neg_eta, input_file_path, tev, 'eta', 'neg', 'full', 'unsorted')
        self.write_df(df_pos_phi, input_file_path, tev, 'phi', 'pos', 'full', 'unsorted')
        self.write_df(df_neg_phi, input_file_path, tev, 'phi', 'neg', 'full', 'unsorted')

        self.write_df(df_pos_eta_sorted_by_phi, input_file_path, tev, 'eta', 'pos', 'full', 'sorted')
        self.write_df(df_pos_phi_sorted_by_phi, input_file_path, tev, 'phi', 'pos', 'full', 'sorted')
        self.write_df(df_neg_eta_sorted_by_phi, input_file_path, tev, 'eta', 'neg', 'full', 'sorted')
        self.write_df(df_neg_phi_sorted_by_phi, input_file_path, tev, 'phi', 'neg', 'full', 'sorted')

        self.write_df(df_pos_eta_a, input_file_path, tev, 'eta', 'pos', 'a', 'unsorted')
        self.write_df(df_pos_eta_b, input_file_path, tev, 'eta', 'pos', 'b', 'unsorted')
        self.write_df(df_pos_eta_c, input_file_path, tev, 'eta', 'pos', 'c', 'unsorted')
        self.write_df(df_pos_eta_d, input_file_path, tev, 'eta', 'pos', 'd', 'unsorted')
        self.write_df(df_pos_eta_e, input_file_path, tev, 'eta', 'pos', 'e', 'unsorted')

        self.write_df(df_neg_eta_a, input_file_path, tev, 'eta', 'neg', 'a', 'unsorted')
        self.write_df(df_neg_eta_b, input_file_path, tev, 'eta', 'neg', 'b', 'unsorted')
        self.write_df(df_neg_eta_c, input_file_path, tev, 'eta', 'neg', 'c', 'unsorted')
        self.write_df(df_neg_eta_d, input_file_path, tev, 'eta', 'neg', 'd', 'unsorted')
        self.write_df(df_neg_eta_e, input_file_path, tev, 'eta', 'neg', 'e', 'unsorted')

        self.write_df(df_pos_phi_a, input_file_path, tev, 'phi', 'pos', 'a', 'unsorted')
        self.write_df(df_pos_phi_b, input_file_path, tev, 'phi', 'pos', 'b', 'unsorted')
        self.write_df(df_pos_phi_c, input_file_path, tev, 'phi', 'pos', 'c', 'unsorted')
        self.write_df(df_pos_phi_d, input_file_path, tev, 'phi', 'pos', 'd', 'unsorted')
        self.write_df(df_pos_phi_e, input_file_path, tev, 'phi', 'pos', 'e', 'unsorted')

        self.write_df(df_neg_phi_a, input_file_path, tev, 'phi', 'neg', 'a', 'unsorted')
        self.write_df(df_neg_phi_b, input_file_path, tev, 'phi', 'neg', 'b', 'unsorted')
        self.write_df(df_neg_phi_c, input_file_path, tev, 'phi', 'neg', 'c', 'unsorted')
        self.write_df(df_neg_phi_d, input_file_path, tev, 'phi', 'neg', 'd', 'unsorted')
        self.write_df(df_neg_phi_e, input_file_path, tev, 'phi', 'neg', 'e', 'unsorted')

        self.write_df(df_pos_eta_sorted_by_phi_a, input_file_path, tev, 'eta', 'pos', 'a', 'sorted')
        self.write_df(df_pos_eta_sorted_by_phi_b, input_file_path, tev, 'eta', 'pos', 'b', 'sorted')
        self.write_df(df_pos_eta_sorted_by_phi_c, input_file_path, tev, 'eta', 'pos', 'c', 'sorted')
        self.write_df(df_pos_eta_sorted_by_phi_d, input_file_path, tev, 'eta', 'pos', 'd', 'sorted')
        self.write_df(df_pos_eta_sorted_by_phi_e, input_file_path, tev, 'eta', 'pos', 'e', 'sorted')

        self.write_df(df_neg_eta_sorted_by_phi_a, input_file_path, tev, 'eta', 'neg', 'a', 'sorted')
        self.write_df(df_neg_eta_sorted_by_phi_b, input_file_path, tev, 'eta', 'neg', 'b', 'sorted')
        self.write_df(df_neg_eta_sorted_by_phi_c, input_file_path, tev, 'eta', 'neg', 'c', 'sorted')
        self.write_df(df_neg_eta_sorted_by_phi_d, input_file_path, tev, 'eta', 'neg', 'd', 'sorted')
        self.write_df(df_neg_eta_sorted_by_phi_e, input_file_path, tev, 'eta', 'neg', 'e', 'sorted')

        self.write_df(df_pos_phi_sorted_by_phi_a, input_file_path, tev, 'phi', 'pos', 'a', 'sorted')
        self.write_df(df_pos_phi_sorted_by_phi_b, input_file_path, tev, 'phi', 'pos', 'b', 'sorted')
        self.write_df(df_pos_phi_sorted_by_phi_c, input_file_path, tev, 'phi', 'pos', 'c', 'sorted')
        self.write_df(df_pos_phi_sorted_by_phi_d, input_file_path, tev, 'phi', 'pos', 'd', 'sorted')
        self.write_df(df_pos_phi_sorted_by_phi_e, input_file_path, tev, 'phi', 'pos', 'e', 'sorted')

        self.write_df(df_neg_phi_sorted_by_phi_a, input_file_path, tev, 'phi', 'neg', 'a', 'sorted')
        self.write_df(df_neg_phi_sorted_by_phi_b, input_file_path, tev, 'phi', 'neg', 'b', 'sorted')
        self.write_df(df_neg_phi_sorted_by_phi_c, input_file_path, tev, 'phi', 'neg', 'c', 'sorted')
        self.write_df(df_neg_phi_sorted_by_phi_d, input_file_path, tev, 'phi', 'neg', 'd', 'sorted')
        self.write_df(df_neg_phi_sorted_by_phi_e, input_file_path, tev, 'phi', 'neg', 'e', 'sorted')

    def write_df(self, df, input_file_path, tev, process, charge, part, data_order):
        file_path, file_name = os.path.split(input_file_path)
        file_ext = '.csv'
        out_put_folder = file_path+'/'+tev
        if not os.path.exists(out_put_folder):
            os.makedirs(out_put_folder)
        output_file_path = out_put_folder+'/'+process+'_'+charge+'_'+part+'_'+data_order+file_ext
        df.to_csv(output_file_path,header=False, index=False)
        print(output_file_path)




