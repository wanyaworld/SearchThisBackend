#!/usr/bin/env python3
import sys
'''from collections import defaultdict
word_count = defaultdict(int)
for line in sys.stdin:
    try:
        line = line.strip()
        word, count = line.split()
        count = int(count)
    except:
        continue
    word_count[word] += count

for word, count in word_count.items():
    print(word, count)
'''

for line in sys.stdin:
	print(line.rstrip())
