import pandas as pd
from scipy.sparse import coo_matrix
from sklearn.utils import shuffle
class SSShuffle:

    def __init__(self):
        print('Shuffle')

    def shuffle_matrix(self, input_file, output_file):
        orig_df = pd.read_csv(input_file, names=['X', 'Y', 'Z'])
        # print(orig_df.head())
        row_co = orig_df['X']
        col_co = orig_df['Y']
        co_value = orig_df['Z']

        mat_coo = coo_matrix((co_value, (row_co, col_co)))
        orig_shape = mat_coo.get_shape()
        linear_shape = orig_shape[0]*orig_shape[1]
        mat_coo_linear = mat_coo.reshape((linear_shape, 1))
        # print(mat_coo_linear)
        # print('gheu')
        mat_coo_linear = shuffle(mat_coo_linear, random_state=0)
        mat_coo = mat_coo_linear.reshape(orig_shape)
        # print(mat_coo)
        row_co_shufle = mat_coo.row
        col_co_shufle = mat_coo.col
        data_co_shufle = mat_coo.data
        shuff_df = pd.DataFrame(columns=['X', 'Y', 'Z'])
        shuff_df['X'] = row_co_shufle
        shuff_df['Y'] = col_co_shufle
        shuff_df['Z'] = data_co_shufle
        shuff_df.to_csv(output_file, header=False, index=None)
        # mat_arr = mat_coo.reshape(shape=(1,))

