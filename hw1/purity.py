
#  THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - RUOCHEN KONG


import os
import math

from closed import loadvoc

def loadDt():
	f = open('result\\word-assignments.dat','r')
	res = []

	for line in f:
		top = set()
		itemtopic = line.strip().split(' ')[1:]

		for it in itemtopic:
			t = it.split(':')[1]
			top.add(int(t))
		res.append(top)
	f.close()

	return res

def matDtt():
	raw = loadDt()

	res = []
	for i in range(5):
		res.append( [0]*5)


	for line in raw:

		for i in range(5):
			for j in range(5):

				if line | {i} == line or line | {j} == line:
					res[i][j] += 1

	return res

def loadPatterns():

	P = []
	for i in range(5):
		dicp = {}
		fn = 'patterns\\patterns-%d.txt'%i
		f = open(fn,'r')

		for line in f:
			row = line.strip().replace('[','').replace(']','').split(' ',1)
			dicp[row[1]] = int(row[0])

		f.close()
		P.append(dicp)
	return P 

def loadTopics():

	T = []
	for i in range(5):
		tmp = []

		fn = 'topic-%d.txt'%i
		f = open(fn,'r')

		for line in f:
			terms = set(line.strip().split(' '))
			tmp.append(terms)

		f.close()
		T.append(tmp)

	return T


def calftp(tp, p):

	pset = set(p.split(' '))
	res = 0

	for line in tp:
		if pset | line == line:
			res += 1

	return res

def calpurity(f,p,T,Dtt,t):

	res = math.log2(f/Dtt[t][t])

	maxr = 0
	for i in range(5):

		if i == t:
			continue

		fp = calftp(T[i],p)
		tmp = (f + fp)/Dtt[t][i]

		if tmp > maxr:
			maxr = tmp
	res -= math.log2(maxr)
	return res


def purot(tid,T,Dtt,P):

	res = {}

	Pt = P[tid]

	for item in Pt.keys():

		f = Pt[item]

		pur = calpurity(f,item,T,Dtt,tid)

		res[item] = pur

	return res

def rerank(P,S):

	res = []

	for k in P.keys():
		r = S[k]*(math.exp(P[k]))

		items = sorted(k.split(' '))

		res.append([r,P[k],items])

	return sorted(res, key = lambda x:x[0], reverse = True)



def outfile(fn,Res,voc):

	f = open(fn,'w')

	fnp = fn+'.phrase'
	fp = open(fnp,'w')

	for res in Res:

		pur = res[1]
		items = res[2]

		fp.write('%.4f ['%pur)

		for i in range(len(items)):

			fp.write(voc[int(items[i])])

			if i != len(items)-1:
				fp.write(' ')

			else:
				fp.write(']\n')


		items = ' '.join(items)
		row = '%.4f [%s]\n'%(pur,items)
		f.write(row)

	f.close()
	fp.close()



def main():

	if not os.path.exists('purity'):
		os.makedirs('purity')

	Top = loadTopics()
	D = matDtt()
	Pat = loadPatterns()
	V = loadvoc()


	for i in range(5):

		pur = purot(i,Top,D,Pat)
		out = rerank(pur,Pat[i])

		n = 'purity\\purity-%d.txt'%i

		outfile(n,out,V)

if __name__ == '__main__':
	main()
