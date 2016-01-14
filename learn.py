#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
scorestr = [
		"(#)",
		"(#)(#)",
		"(#)(#)(#)",
		"(#)(#)(#)(#)",
		"(#)(#)(#)(#)(#)",
		"(#)(#)(#)(#)(#)(#)",
		"(#)(#)(#)(#)(#)(#)(#)",
		"(#)(#)(#)(#)(#)(#)(#)(#)",
		"(#)(#)(#)(#)(#)(#)(#)(#)(#)",
		"(#)(#)(#)(#)(#)(#)(#)(#)(#)(#)"
	]
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
zenbu = 0
q = open("points.data","r")
zenbu = len(q.read().split("\n")) - 1
f = open("points.data","r")
g = open("teacher.data","a")
for q,i in enumerate(f.readlines()):
	os.system("clear")
	print "+++++++++++++++++++++++++++今回のプレゼン++++++++ " + str(q) + "/" + str(zenbu) + " ++++++++++++++++++++++"
	for count,k in enumerate(i.strip().split(",")):
		if count == 0:
			print "この発表は元気が良かったか？" + "\t" + scorestr[int(float(k)) - 1]
		elif count == 1:
			print "スライドの内容はどうだったか？" + "\t" + scorestr[int(float(k)) - 1]
		elif count == 2:
			print "プレゼンの仕方はどうだったか？" + "\t" + scorestr[int(float(k)) - 1]
		elif count == 3:
			print "質問回数はどうか？" + "\t" + "\t" + scorestr[int(float(k)) - 1]
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print "---------------------------------"
	for co,p in enumerate(bages):
		print p +  "-->" + str(co + 1)
	print "---------------------------------"
	print "どのようなプレゼンでしたか？",
	teacher = sys.stdin.readline()
	g.write(teacher)
	

