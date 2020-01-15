import pandas as pd
import os
from sklearn.utils import shuffle


class SuperSymEtaPhi:

    def __init__(self):
        print('Eta Phi Extaction')

    def extraxt_eta_phi_dimuon(self, input_file_path):
        file_path, file_name = os.path.split(input_file_path)
        file_name_without_ext = os.path.splitext(file_name)
        extracted_eta_file = file_path+'/'+file_name_without_ext[0]+'_eta'+file_name_without_ext[1]
        extracted_phi_file = file_path+'/'+file_name_without_ext[0]+'_phi'+file_name_without_ext[1]
        extracted_eta_shuf_file = file_path+'/'+file_name_without_ext[0]+'_eta_shuf'+file_name_without_ext[1]
        extracted_phi_shuf_file = file_path+'/'+file_name_without_ext[0]+'_phi_shuf'+file_name_without_ext[1]
        orig_df = pd.read_csv(input_file_path, delimiter=',')
        orig_df_eta = orig_df['Eta']
        orig_df_phi = orig_df['Phi']

        orig_df_eta_shuf = shuffle(orig_df_eta)
        orig_df_phi_shuf = shuffle(orig_df_phi)
        orig_df_eta.to_csv(extracted_eta_file, header=False, index=False)
        orig_df_phi.to_csv(extracted_phi_file, header=False, index=False)
        orig_df_eta_shuf.to_csv(extracted_eta_shuf_file, header=False, index=False)
        orig_df_phi_shuf.to_csv(extracted_phi_shuf_file, header=False, index=False)

        print(extracted_eta_file)
        print(extracted_phi_file)

