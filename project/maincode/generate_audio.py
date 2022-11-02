import librosa as la
import os 
import numpy as np

outpath = '../data/train_npy'
if not os.path.exists(outpath):
    os.makedirs(outpath)
    
filenames = os.listdir('../data/train')
N = len(filenames)

for i in range(N):
    fn = filenames[i]
    signal, _ = la.load('../data/train/'+fn, sr = 100)
    outname = outpath +'/'+ fn.split('.')[0] + '.npy'
    sig = np.array(list(signal))
    np.save(outname,sig)
    print(i, outname)


#19630