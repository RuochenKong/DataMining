
#  THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - RUOCHEN KONG

import os

from closed import load
from closed import loadvoc

def maxP(Data):
	res = []

	for k in Data.keys():
		
		items = Data[k]

		for y in items:
			new = True
			
			for i in range(len(res)):

				supx = res[i][0]
				x = res[i][1]

				if x | y == y:
					res[i][0] = k
					res[i][1] = y
					new = False
					break
			if new:
				res.append([k,y])

	return sorted(res, key = lambda x:x[0], reverse = True)


def outfile(fn,Res,voc):
	f = open(fn,'w')

	fnp = fn+'.phrase'
	fp = open(fnp,'w')


	for res in Res:
		sup = res[0]
		items = res[1:]

		for t in items:

			item = sorted(list(t))

			fp.write('%d ['%sup)
			for i in range(len(item)):
				fp.write(voc[int(item[i])])

				if i != len(item)-1:
					fp.write(' ')

				else:
					fp.write(']\n')


			item = ' '.join(item)
			row = '%d [%s]\n'%(sup,item)
			f.write(row)

	f.close()
	fp.close()

def main():

	if not os.path.exists('max'):
		os.makedirs('max')

	V = loadvoc()
	for i in range(5):
		n = 'max\\max-%d.txt'%i
		outfile(n,maxP(load(i)),V)
		print(i)


if __name__ == '__main__':
	main()