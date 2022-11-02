import os
import numpy as np
import librosa as la
import madmom as mm

path = '../data/train/'

fns = os.listdir(path)

shortes = 10**7
for fn in fns:
	print(fn, end = ' ')
	signals, _ = la.load(path+fn)
	sig = np.array(signals)
	if len(sig) < shortes:
		shortes = len(sig)
		print(shortes, end = ' ')
	print()