from Mergeeta import Mergeeeta
from Muonml import Muonml
from SuperSymmetry import SuperSymmetry

# mg = Mergeeeta()
#mg.read_and_merge_phi()
# mg.plot_eta()
# mg.divide_eta()
# mg.divide_phi()
# mg.save_phi_for_corr_eta()
# mg.sort_shuffle_divide_phi_by_eta()
# mm = Muonml()
# mm.read_muon_data()
dimuon_raw_7TEV_file = '/home/dgrfi/MEGA/supersymmetry/DiMu7Txyz1L.csv'
dimuon_raw_8TEV_file = '/home/dgrfi/MEGA/supersymmetry/DiMu8Txyz1L.csv'
ss_raw_file = '/home/dgrfi/MEGA/supersymmetry/ss90k.csv'
delim_comma = ','
delim_semicolon = ';'
ss = SuperSymmetry()
ss.read_raw_and_write_SS_momentums()