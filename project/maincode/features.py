import os
import numpy as np
import librosa as la

def stft(sig):
	stft = la.feature.chroma_stft(y=sig, n_fft = 8)
	res = stft[:,:20]
	res = list(res.flatten())
	#print('stft done', len(res))
	return res

def zcrossing(sig):
	zc = la.zero_crossings(y = sig)
	#print('zCross done')
	return len(zc[zc])/len(zc)

def valuesfromF(arrays, hp = False):
	res = []
	if not hp:
		res.append(np.max(arrays))
		res.append(np.min(arrays))
	res.append(np.mean(arrays))
	res.append(np.std(arrays))
	return res

def threeFeatures(sig, hp = False):
	rms = la.feature.rms(y = sig)
	centroid = la.feature.spectral_centroid(y = sig)
	flat = la.feature.spectral_flatness(y = sig)
	res = valuesfromF(rms, hp) + valuesfromF(centroid , hp) + valuesfromF(flat, hp)
	#print('rms, centroid, flat done',len(res))
	return res

def mfcc(sig):
	mc = la.feature.mfcc(y = sig)
	res = []
	for i in range(20):
		res += valuesfromF(mc[i])
	#print('mfcc done', len(res))
	return res

def features(sig):
	tempo, _ = la.beat.beat_track(y=sig)
	res = [tempo]
	res += stft(sig)
	res.append(la.estimate_tuning(y = sig))
	res.append(zcrossing(sig))
	res += threeFeatures(sig)
	res += mfcc(sig)
	res += list(la.autocorrelate(sig, max_size=170))

	sigh,sigp = la.effects.hpss(sig)
	res += threeFeatures(sigh,True)
	res.append(la.beat.beat_track(y=sigh)[0])
	res.append(zcrossing(sigh))

	res += threeFeatures(sigp,True)
	res.append(la.beat.beat_track(y=sigp)[0])
	res.append(zcrossing(sigp))

	return np.array(res)



outpath = '../data/features'
if not os.path.exists(outpath):
	os.makedirs(outpath)


path = '../data/train/'
fns = os.listdir(path)
N = len(fns)

def files(start):
	end = min(start+3000,N)
	for i in range(start, end):
		fn = fns[i]

		signals, _ = la.load(path+fn)
		sid = fn.split('.')[0]
		np.save('%s/%s.npy'%(outpath,sid),features(signals))
		print(i,'done')

files(21000)