import numpy as np
import soundfile as sf
import os

def normalize(x):
	return (x-np.min(x))/(np.max(x)-np.min(x))

path = '../data/train/'
filenames = os.listdir(path)
labels = np.load('../data/labels.npy')

corrAll = []
corr = []
for i in range(20):
	corr.append([])

N = len(filenames)

for i in range(N):
	print(i)
	fn = path+filenames[i]
	data, samplerate = sf.read(fn)
	d = np.array(data)
	if len(d.shape) == 1:
		cor = 0
	else:
		d = d.T
		c1 = normalize(d[0])
		c2 = normalize(d[1])

		cor = np.linalg.norm(c1-c2,2)

	corrAll.append(cor)
	ind = labels[i]
	corr[19].append(cor) if ind == -1 else corr[ind].append(cor)

	

p = '../data/'
if not os.path.exists(p +'corr'):
	os.makedirs(p +'corr')

p += 'corr/'
np.save(p+'all.npy',np.array(corrAll))

for i in range(19):
	np.save(p+'%02d.npy'%i,np.array(corr[i]))
np.save(p+'unknown.npy',np.array(corr[19]))