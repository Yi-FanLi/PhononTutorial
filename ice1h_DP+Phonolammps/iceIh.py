# API example to calculate finite temperature (300K) force constants
# using dynaphopy (quasiparticle theory)

import os
from phonolammps import Phonolammps
from phonopy import Phonopy
import phonopy
#from dynaphopy.interface.lammps_link import generate_lammps_trajectory
#from dynaphopy.interface.phonopy_link import ForceConstants
#from dynaphopy import Quasiparticle
#from dynaphopy.atoms import Structure

import numpy as np

# calculate harmonic force constants with phonoLAMMPS
print("trying to initialize phlammps")
phlammps = Phonolammps('in.lammps',
                       supercell_matrix=np.diag([2, 2, 2])
                       )

print("phlammps initialized")

unitcell = phlammps.get_unitcell()

print(unitcell)
np.save("unitcell.npy", unitcell, allow_pickle=True)

# print("getting force constants")

# os.system("ls -l")
# os.system("sleep 5")
force_constants = phlammps.get_force_constants()#include_data_set=True)
# print("got force constants")
# print("shape:")
# print(force_constants.shape)
# print("value:")
# print(force_constants)
# np.save("force_constants.npy", force_constants)
supercell_matrix = phlammps.get_supercell_matrix()

phlammps.write_force_constants()
phlammps.write_force_sets()
phlammps.write_unitcell_POSCAR()
# print("supercell matrix:")
# print(supercell_matrix)
# np.save("supercell_matrix.npy", supercell_matrix, allow_pickle=True)
#
# phonon = phonopy.load(supercell_matrix=np.diag([1, 1, 1]), unitcell_filename="POSCAR")
# phonon.set_mesh([20, 20, 20])


# phlammps.plot_phonon_dispersion_bands()

## set force constants for dynaphopy
#force_constants = ForceConstants(phlammps.get_force_constants(),
#                                 supercell=phlammps.get_supercell_matrix())
#
## Print harmonic force constants
#print('harmonic force constants')
#print(force_constants.get_array())
#
#structure = phlammps.get_unitcell()
#
#
## define structure for dynaphopy
#dp_structure = Structure(cell=structure.get_cell(),  # cell_matrix, lattice vectors in rows
#                         scaled_positions=structure.get_scaled_positions(),
#                         atomic_elements=structure.get_chemical_symbols(),
#                         primitive_matrix=phlammps.get_primitve_matrix(),
#                         force_constants=force_constants)
#
## calculate trajectory for dynaphopy with lammps
#trajectory = generate_lammps_trajectory(dp_structure, 'in.lammps',
#                                        total_time=20,      # ps
#                                        time_step=0.001,    # ps
#                                        relaxation_time=5,  # ps
#                                        silent=False,
#                                        supercell=[2, 2, 2],
#                                        memmap=False,
#                                        velocity_only=True,
#                                        temperature=300)
#
## set dynaphopy calculation
#calculation = Quasiparticle(trajectory)
#calculation.select_power_spectra_algorithm(2)  # select FFT algorithm
#
#calculation.get_renormalized_phonon_dispersion_bands()
#renormalized_force_constants = calculation.get_renormalized_force_constants()
#
## Print phonon band structure
#calculation.plot_renormalized_phonon_dispersion_bands()
#
## Plot linewidths vs frequencies (interpolated to a mesh 20x20x20)
## calculation.parameters.mesh_phonopy = [20, 20, 20]
## calculation.plot_frequencies_vs_linewidths()
## calculation.write_mesh_data()
#
## Print renormalized force constants
#print('renormalized force constants at 300K')
#print(renormalized_force_constants.get_array())
