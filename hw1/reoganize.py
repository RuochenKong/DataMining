
#  THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - RUOCHEN KONG

import os

f = open('result\\word-assignments.dat','r')
T = []

for i in range(5):
	T.append(open('topic-%d.txt'%i,'w'))

for line in f:
	termsLoc = line.strip().split(' ')[1:]
	Temp = [[],[],[],[],[]]
	for t in termsLoc:
		term,loc = t.split(':')
		loc = int(loc)
		Temp[loc].append(term)
	for i in range(5):
		if len(Temp[i]) != 0:
			T[i].write(' '.join(Temp[i]))
			T[i].write('\n')

for i in range(5):
	T[i].close()

f.close()