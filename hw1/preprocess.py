
#  THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - RUOCHEN KONG


fn = 'paper.txt'
f = open(fn,encoding='UTF-8')
voc = []
title = open('title.txt','w')
for line in f:
	try:
		terms = line.strip().split('\t')[1].split(' ')
	except:
		title.write('0\n')
		continue

	titDic = {}

	for t in terms:
		if t not in voc:
			voc.append(t)

		if t in titDic:
			titDic[t] += 1
		else:
			titDic[t] = 1

	uniq = titDic.keys()
	title.write('%d'%len(uniq))

	for t in uniq:
		title.write(' %d:%d'%(voc.index(t),titDic[t]))
	title.write('\n')

title.close()
f.close()


vocab = open('vocab.txt','w')
for v in voc:
	vocab.write(v)
	vocab.write('\n')
vocab.close()