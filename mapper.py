#!/usr/bin/env python3 
import sys 
import string 
import json
from collections import deque

lookwards = 3
prvs = deque()
found = 0
nexts = []
added = 0
filename = ""

for line in sys.stdin:
	if filename == "":
		filename = line.rstrip()
	line = line.strip() 
	words = line.split() 
	for w in words: 
		if found == 1:
			if added >= lookwards:
				break
			nexts.append(w)
			added += 1
		else:
			table = w.maketrans('', '', string.punctuation)
			w = w.translate(table).lower() 
			if len(prvs) > lookwards:
				prvs.popleft()
			if w == sys.argv[1]:
				found = 1
			prvs.append(w)

res = ""
if found == 1:
	for prv in prvs:
		res += prv + ' '
	for next in nexts:
		res += next + ' '
jsonResult ={ "url": filename, "result": res }
print(jsonResult)
#print(JSON.stringify(jsonResult))
