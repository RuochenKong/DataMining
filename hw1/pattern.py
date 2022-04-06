
#  THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - RUOCHEN KONG

import os


# join the scanned itemset to form the larger set
def ciSet(prevset):
	res = []
	for i in range(len(prevset)-1):
		for j in range(i+1,len(prevset)):
			new = prevset[i]|prevset[j]
			if new not in res:
				res.append(new)
	return res



# the iteration step of Apriori
def apitr(prevset, D, threshold):

	items = ciSet(prevset)
	res = {}
	newitems = []
	for item in items:
		num = 0
		for line in D:
			if item | line == line:
				num += 1
		key = ' '.join(sorted(list(item)))
		if num >= threshold:
			res[key] = num
			newitems.append(item)
	return res,newitems



def aprior(topicid,min_sup):

	# load data from 'topic-i.txt'
	f = open('topic-%d.txt'%topicid,'r')

	itemSup = {} # frequent pattern
	Data = [] # collection of itemsets
	N = 0 # number of lines 
	for line in f:
		N += 1
		t = line.strip().split(' ')
		Data.append(set(t))
		for i in t:
			if i in itemSup:
				itemSup[i] += 1
			else:
				itemSup[i] = 1
	f.close()
	minsupNum = int(N * min_sup)

	# load vocab
	f = open('vocab.txt','r')
	vocab = []
	for line in f:
		vocab.append(line.strip())

	f.close()


	# remove the ones with sup < min_sup
	delet = []
	for k,v in itemSup.items():
		if v < minsupNum:
			delet.append(k)

	for k in delet:
		del itemSup[k]

	iset = []
	for i in itemSup.keys():
		iset.append({i})


	# Start Apriori iteratively until no super frequent pattern
	remain = 100
	while remain > 0:
		newSup,iset = apitr(iset,Data,minsupNum)
		itemSup.update(newSup)
		remain = len(newSup.keys())
		print(remain)


	# output into files
	out = sorted(itemSup.items(), key = lambda x:x[1], reverse = True)
	outfn = 'patterns\\patterns-%d.txt'%topicid
	fout = open(outfn,'w')

	outfn = 'patterns\\patterns-%d.txt.phrase'%topicid
	foutPhrase = open(outfn,'w')

	for i,supnum in out:
		row = '%d [%s]\n'%(supnum,i)
		fout.write(row)

		foutPhrase.write('%d ['%supnum)
		phrase = i.split(' ')
		for p in range(len(phrase)):
			foutPhrase.write(vocab[int(phrase[p])])
			if p != len(phrase)-1:
				foutPhrase.write(' ')
		foutPhrase.write(']\n')

	fout.close()
	foutPhrase.close()

def main():
	if not os.path.exists('patterns'):
		os.makedirs('patterns')

	for i in range(5):
		aprior(i,0.01)

if __name__ == '__main__':
	main()