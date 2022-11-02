import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

choices = ['norm','origin','filter']

path = {'norm':'normalized', 'origin':'processed_train', 'filter': 'norm_filtcorr'}

dataform = choices[2]

y = np.load('../data/train_labels.npy')
X = np.load('../data/%s.npy'%path[dataform])
X = np.nan_to_num(X)


X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)


np.save('../results/keras_%s/xtrain.npy'%(dataform),X_train)
np.save('../results/keras_%s/ytrain.npy'%(dataform),y_train)
np.save('../results/keras_%s/xtest.npy'%(dataform),X_test)
np.save('../results/keras_%s/ytest.npy'%(dataform),y_test)

def RF(folder = 'norm'):
	for i in range(10):
		clf = RandomForestClassifier( class_weight = 'balanced', random_state = i)
		clf.fit(X_train,y_train)

		yhat = clf.predict(X_test)

		np.save('../results/%s/RF_rand%d_yhat.npy'%(folder,i),yhat)
		print('random_state: %d done'%i)

def knn(folder = 'norm'):
	for i in range(21,41):
		neigh = KNeighborsClassifier(n_neighbors=i)
		neigh.fit(X_train, y_train)

		yhat = neigh.predict(X_test)

		np.save('../results/%s/knn%d_yhat.npy'%(folder,i),yhat)
		print('kNN: %d done'%i)

def mlp(folder = 'norm'):
	for i in range(10):
		clf = MLPClassifier(random_state=i, max_iter=300).fit(X_train, y_train)
		yhat = clf.predict(X_test)

		np.save('../results/%s/mlp_rand%d_yhat.npy'%(folder,i),yhat)
		print('random_state: %d done'%i)

#RF('norm_filter')
#mlp('norm_filter')




#np.save('../results/ytest.npy',y_test)
