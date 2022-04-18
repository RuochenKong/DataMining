import os 
import numpy as np

fns = os.listdir('../data/train')
labels = np.load('../data/labels.npy')

res = []

for f in fns:
	sid = int(f.split('.')[0])
	res.append(labels[sid])
	print(sid)

np.save('../data/train_labels.npy',np.array(res))