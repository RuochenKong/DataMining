import os
import numpy as np

path = '../data/train_npy/'

fns = os.listdir(path)

D = []
for i in range(5000):
	aud = np.load(path + fns[i])
	aud.resize((660000,1))
	print(aud.shape)
	D.append(aud)
	print(i,'done')

D = np.array(D)
print(D.shape)
np.save('../data/audio.npy',D)