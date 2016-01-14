#!/usr/bin/python

from sklearn import svm
from sklearn import datasets

di = datasets.load_digits()
print di.data
print di.target

clf = svm.SVC(gamma=0.001, C=100)
clf.fit(di.data[:-1], di.target[:-1])
print clf.predict(di.data[-1])

