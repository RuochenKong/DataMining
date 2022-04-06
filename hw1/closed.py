
#  THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - RUOCHEN KONG

import os

def load(tid):
	res = {}
	fn = 'patterns\\patterns-%d.txt'%tid
	f = open(fn,'r')

	for line in f:
		tmp = line.replace('[','').replace(']','')
		tmp = tmp.strip().split(' ')
		sup = int(tmp[0])
		items = set(tmp[1:])

		if sup in res:
			res[sup].append(items)
		else:
			res[sup] = [items]
	f.close()

	return res

def closedP(Data):
	for k in Data.keys():
		kitems = Data[k]
		if len(kitems) < 2:
			continue
		for i in range(len(kitems)):
			for j in range(len(kitems)):
				if i != j and kitems[i] | kitems[j] == kitems[j]:
					kitems.remove(kitems(i))
					i -= 1
					break
	return Data



def loadvoc():
	f = open('vocab.txt','r')
	vocab = []
	for line in f:
		vocab.append(line.strip())
	f.close()
	return vocab

def outfile(fn,Res,voc):
	f = open(fn,'w')

	fnp = fn+'.phrase'
	fp = open(fnp,'w')


	for k in Res.keys():
		sup = k
		items = Res[k]

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

	if not os.path.exists('closed'):
		os.makedirs('closed')

	V = loadvoc()
	for i in range(5):
		n = 'closed\\closed-%d.txt'%i
		outfile(n,closedP(load(i)),V)
		print(i)

if __name__ == '__main__':
	main()
