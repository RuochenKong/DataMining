import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


y = np.load('../data/train_labels.npy')
X = np.load('../data/normalized.npy')


X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

clf = SVC(decision_function_shape='ovo')
clf.fit(X_train,y_train)
yhat = clf.predict(X_test)

np.save('../results/svm_yhat.npy',yhat)

