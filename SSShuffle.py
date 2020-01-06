import pandas as pd
from scipy.sparse import coo_matrix
from sklearn.utils import shuffle
class SSShuffle:

    def __init__(self):
        print('Shuffle')

    def shuffle_matrix(self, input_file):
        orig_df = pd.read_csv(input_file,names=['X', 'Y', 'Z'])
        # print(orig_df.head())
        row_co = orig_df['X']
        col_co = orig_df['Y']
        co_value = orig_df['Z']

        mat_coo = coo_matrix((co_value, (row_co, col_co)))

        mat_coo = shuffle(mat_coo, random_state=0, n_samples=2)
        print(mat_coo)
        # print(sdf.head())
