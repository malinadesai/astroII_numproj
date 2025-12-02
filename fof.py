import matplotlib.pyplot as plt
import numpy as np # useful for calculations
import h5py #required to read hdf5 files
import matplotlib as mpl
from fastdist import fastdist 

from scipy.spatial.distance import cdist

import pdb
FloatType = np.float64  # double precision: np.float64, for single use np.float32

def read_gadget_snapshot(file_name):
	data = h5py.File(file_name, 'r')  # load full hdf5 file

	time = FloatType(data['Header'].attrs['Time']) # the scale factor at which snapshot was written
	BoxSize = FloatType(data['Header'].attrs['BoxSize']) # box size in code units (Mpc)

	Pos = np.array(data['PartType1']['Coordinates'], dtype=FloatType) #3d Positions of all particles, e.g. x coord: Pos[:,0]

	mass = FloatType(data['Header'].attrs['MassTable'][1]) # mass of one DM particle

	n_particles = Pos.size // 3

	return time, Pos, mass, n_particles, BoxSize


file_name = "snapshot_002.hdf5"

time, Pos, mass, n_particles, BoxSize = read_gadget_snapshot(file_name)

print("Scale factor: %g  (should be 1)" %(time))

box_vol = BoxSize**3
mean_dist = (box_vol/n_particles)**(1/3) # mean distance between particles
print('mean distance between particles = {}'.format(mean_dist))

# sanity check visualizing structure formation
x=Pos[:, 0]
y=Pos[:, 1]
z=Pos[:, 2]

plt.hist2d(x, y, bins = 1000,  norm=mpl.colors.LogNorm())
# plt.show()

# FoF algorithm
linking_length = mean_dist*0.2

# find distance between particle i and particle j
def particle_distance(i, j, positions):
    x_i, y_i, z_i = positions[i, 0], positions[i, 1], positions[i, 2]
    x_j, y_j, z_j = positions[j, 0], positions[j, 1], positions[j, 2]
    return np.sqrt((x_i - x_j)**2 + (y_i - y_j)**2 + (z_i - z_j)**2)






=======
# pairwise_distances = cdist(Pos, Pos)
pairwise_distances = fastdist.euclidean(Pos, Pos)
print('done')
>>>>>>> b39b1ac53d50028d7f7d38300b1a99cc4fd421c3


