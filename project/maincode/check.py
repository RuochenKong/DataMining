import numpy as np
import soundfile as sf
import os

def normalize(x):
	return (x-np.min(x))/(np.max(x)-np.min(x))

path = '../data/train/'
filenames = os.listdir(path)


i = 178
fn = path+filenames[i]
data, samplerate = sf.read(fn)
data = np.array(data)
print(len(data.shape))
d = np.array(data).T
print(d[0])
c1 = normalize(d[0])
c2 = normalize(d[1])

print(c1.shape, c2.shape)
cor = np.linalg.norm(c1-c2,2)

