from Mergeeta import Mergeeeta
from Muonml import Muonml
from SuperSymmetry import SuperSymmetry
from SSShuffle import SSShuffle

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

run_env = 'bhaduri'
dimuon_orig_file = '/home/'+run_env+'/MEGA/supersymmetry/Data/Dimoun_SS/DiMu7T_xy_z_out.csv'
ssshuf = SSShuffle()
ssshuf.shuffle_matrix(dimuon_orig_file)