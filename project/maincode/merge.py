import numpy as np
import os 

path = '../data/'
correlation = np.load(path+'corr/all.npy')

D = []

fpath = path+'features/'
filenames = os.listdir(fpath)

N = len(filenames)

for i in range(N):
	fn = fpath+filenames[i]
	f = np.append(np.load(fn),correlation[i])
	D.append(f)
	print(i,'done')

np.save(path+'train_features.npy',np.array(D))