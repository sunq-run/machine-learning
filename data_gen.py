#!/usr/bin/python
import random
f = open("points.data","a")
data = ""
for i in range(30):
	data = ""
	for count,k in enumerate(range(4)):
		if count == 3:
			data = data + str(float(random.randint(1,10))) + "\n"
		else:
			data = data + str(float(random.randint(1,10))) +","
	f.write(data)

f.close

