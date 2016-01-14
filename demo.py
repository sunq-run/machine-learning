#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn import svm
from sklearn import datasets
import sys 
argv = sys.argv
target = [float(argv[1]),float(argv[2]),float(argv[3]),float(argv[4])]
points = []
f = open("points.data","r")

for i in f.readlines():
	points.append(i.strip().split(","))

bages = [	
	 "元気がいいバッジ",
	 "元気がいいがスライド微妙バッジ",
	 "スライドいいバッジ",
	 "スライドいいけど元気がないなバッジ",
	 "質問おおいねバッジ",
	 "全体的にいいね",
	 "質問が少ないあとまあまあバッジ",
	 "全然だめねバッジ",
	 "プレゼンがすばらしいバッジ"
	 ]
	

di = datasets.load_digits()
# [元気か　、スライド、プレゼン、質問回数
le = [6,9,2,6,1,2,2,1,1,8,5,9,6,9,6,2,7,6,9,9,8,9,3,3,6,6,7,2,6,3]
print "今までの評価-->" + str(points)
print "毎回の発表の実際の評価-->" + str(le)


clf = svm.SVC(gamma=0.001, C=100)
clf.fit(points, le)
print clf.predict(target)
print bages[clf.predict(target)[0]-1]
