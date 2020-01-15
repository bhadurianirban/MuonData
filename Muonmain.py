from Mergeeta import Mergeeeta
from Muonml import Muonml
from SuperSymmetry import SuperSymmetry
from SSShuffle import SSShuffle
from SusmitaShuff import SusmitaShuff
from BumbuSin import BumbuSin

# mg = Mergeeeta()
#mg.read_and_merge_phi()
# mg.plot_eta()
# mg.divide_eta()
# mg.divide_phi()
# mg.save_phi_for_corr_eta()
# mg.sort_shuffle_divide_phi_by_eta()
# mm = Muonml()
# mm.read_muon_data()


# run_env = 'bhaduri'
# dimuon_raw_7TEV_file = '/home/'+run_env+'/MEGA/supersymmetry/DiMu7Txyz1L.csv'
# dimuon_raw_8TEV_file = '/home/'+run_env+'/MEGA/supersymmetry/DiMu8Txyz1L.csv'
# ss_raw_file = '/home/'+run_env+'/MEGA/supersymmetry/ss90k.csv'
#
# ss = SuperSymmetry()
# dimuon_files = ss.reorder_Px_Py_Pz(dimuon_raw_7TEV_file, 'DiMu7T_', ';')
# for dimuon_file in dimuon_files :
#     ss.read_raw_and_write_dimoun_momentums(dimuon_file)

# run_env = 'dgrfi'
# dimuon_orig_file_prefix = '/home/'+run_env+'/MEGA/supersymmetry/Data/Dimoun_SS/SS_'
# dimuon_orig_file_suffixes = ['xy_z_out.csv','xz_y_out.csv','yz_x_out.csv']
# dimuon_shuf_file_suffixes = ['xy_z_shuf.csv','xz_y_shuf.csv','yz_x_shuf.csv']
#
#
# ssshuf = SSShuffle()
# for i in range(3):
#     dimuon_orig_file = dimuon_orig_file_prefix + dimuon_orig_file_suffixes[i]
#     dimuon_shuf_file = dimuon_orig_file_prefix + dimuon_shuf_file_suffixes[i]
#     ssshuf.shuffle_matrix(dimuon_orig_file, dimuon_shuf_file)

# sus_shuf = SusmitaShuff()
# sus_shuf.shuffle_z('/home/bhaduri/MEGA/supersymmetry/SSfiles/DiMu7xyz.csv','/home/bhaduri/MEGA/supersymmetry/SSfiles/DiMu7xyz_shuf.csv')
# sus_shuf.shuffle_z('/home/bhaduri/MEGA/supersymmetry/SSfiles/DiMu7yzx.csv','/home/bhaduri/MEGA/supersymmetry/SSfiles/DiMu7yzx_shuf.csv')
# sus_shuf.shuffle_z('/home/bhaduri/MEGA/supersymmetry/SSfiles/DiMu7zxy.csv','/home/bhaduri/MEGA/supersymmetry/SSfiles/DiMu7zxy_shuf.csv')
# sus_shuf.shuffle_z('/home/bhaduri/MEGA/supersymmetry/SSfiles/ssxyz50.csv','/home/bhaduri/MEGA/supersymmetry/SSfiles/ssxyz50_shuf.csv')
# sus_shuf.shuffle_z('/home/bhaduri/MEGA/supersymmetry/SSfiles/ssyzx50.csv','/home/bhaduri/MEGA/supersymmetry/SSfiles/ssyzx50_shuf.csv')
# sus_shuf.shuffle_z('/home/bhaduri/MEGA/supersymmetry/SSfiles/sszxy50.csv','/home/bhaduri/MEGA/supersymmetry/SSfiles/sszxy50_shuf.csv')

bumbusin  = BumbuSin()
bumbusin.plot_sine()