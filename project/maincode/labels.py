import numpy as np
import os

fn = '../data/train.csv'
f = open(fn)

L = []

ind = []
i = 0
head = 1
for line in f:
	if head:
		head = 0
		continue
	values = line.strip().split(',')
	L.append([int(values[0]),int(values[3])])
	ind.append(int(values[0]))

check = list(range(25000))

for c in check:
	if c not in ind:
		print('Missing: %d'%c)
		L.append([c,-1])

L.sort(key = lambda x: x[0])

label = []

for d,v in L:
	label.append(v)

label = np.array(label)
np.save('../data/labels.npy',label)