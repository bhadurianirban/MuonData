import pandas as pd
from scipy.sparse import coo_matrix
from sklearn.utils import shuffle
from sklearn.utils import resample
from SuperSymmetry import SuperSymmetry

class SusmitaShuff:
    def __init__(self):
        print('SusmitaShuff')

    def shuffle_z(self,momentum_in_file,momentum_shuf_file):
        momentum_xyz = pd.read_csv(momentum_in_file, header=None, names=['X', 'Y', 'Z'])

        # ssdraw = SuperSymmetry()
        # ssdraw.plt_3d_momentum(momentum_xyz)
        z_col = momentum_xyz['Z']
        z_shuff = shuffle(z_col)
        z_shuff = z_shuff.reset_index(drop=True)
        # print(z_shuff)

        momentum_xyz['Z'] = z_shuff
        momentum_xyz.to_csv(momentum_shuf_file, header=None,index=False)

        # ssdraw.plt_3d_momentum(momentum_xyz)
        # momentum_xyz_pos = momentum_xyz - momentum_xyz.min()
        # print(momentum_xyz_pos.shape)
        # momentum_xyz_pos = momentum_xyz_pos.sort_values(['X', 'Y']).drop_duplicates(['X', 'Y']).reset_index(drop=True)
        # print(momentum_xyz_pos.shape)
        # row_co = momentum_xyz_pos['X']
        # col_co = momentum_xyz_pos['Y']
        # co_value = momentum_xyz_pos['Z']
        #
        # mat_coo = coo_matrix((co_value, (row_co, col_co)))
        # orig_shape = mat_coo.get_shape()
        #
        # linear_shape = orig_shape[0] * orig_shape[1]
        # mat_coo_linear = mat_coo.reshape(linear_shape)
        # mat_coo_linear = shuffle(mat_coo_linear, random_state=5)
        # # print(mat_coo_linear)
        # mat_coo = mat_coo_linear.reshape(orig_shape)
        # # print(mat_coo)
        # row_co_shufle = mat_coo.row
        # col_co_shufle = mat_coo.col
        # data_co_shufle = mat_coo.data
        # shuff_df = pd.DataFrame(columns=['X', 'Y', 'Z'])
        # shuff_df['X'] = row_co_shufle
        # shuff_df['Y'] = col_co_shufle
        # shuff_df['Z'] = data_co_shufle
        # shuff_df_orig = shuff_df + momentum_xyz.min()
        # print(shuff_df)
        # shuff_df.to_csv(output_file, header=False, index=None)