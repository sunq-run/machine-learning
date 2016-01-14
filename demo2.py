#!/usr/bin/python
# -*- coding: utf-8 -*-
from sklearn import svm
from sklearn import datasets
import sys 
argv = sys.argv
target = [float(argv[1]),float(argv[2]),float(argv[3]),float(argv[4])]
points = []
le = []
g = open("teacher.data","r")
for d in g.readlines():
	le.append(int(d.strip()))

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
print "今までの評価-->" + str(points)
print "毎回の発表の実際の評価-->" + str(le)


clf = svm.SVC(gamma=0.001, C=100)
clf.fit(points, le)
print clf.predict(target)
print bages[clf.predict(target)[0]-1]
