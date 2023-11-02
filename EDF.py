import numpy as np
import mne
edf = mne.io.read_raw_edf('2.edf')
header = ','.join(edf.ch_names)
np.savetxt('2.csv', edf.get_data().T, delimiter=',', header=header)