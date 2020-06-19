import pandas as pd
from sklearn.utils import shuffle
import os as os

class EPJA:
    def __init__(self):
        print("EPJA")

    def epja_shuffle(self):
        folder7TeV = '/home/bhaduri/Documents/EPJA/8TeV'
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(folder7TeV):
            for file in f:
                if '.txt' in file:
                    files.append(os.path.join(r, file))

        # for f in files:
        #     print(f)
        self.epfa_shuff_files(files)

    def epfa_shuff_files(self, files):
        for f in files:
            contaning_folder = os.path.dirname(f)
            file_name = os.path.basename(f)
            file_name_parts = file_name.split('.')
            out_file_name = contaning_folder+os.path.sep+file_name_parts[0]+'_shuff.csv'

            self.epja_shuff_write_files(f, out_file_name,10)

    def epja_shuff_write_files(self, in_file, out_file, total_shuff_count):
        orig_df = pd.read_csv(in_file, header=None)
        shuffle_df = shuffle(orig_df)
        for shuff_counter in range(total_shuff_count-1):
            print("Shuffling : " + str(shuff_counter))
            shuffle_df = shuffle(shuffle_df)
        print(orig_df.head())
        print(shuffle_df.head())
        print(out_file)
        shuffle_df.to_csv(out_file,index=None,header=None)

