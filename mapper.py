#!/usr/bin/env python3 
import sys 
import string 
for line in sys.stdin: 
    line = line.strip() 
    words = line.split() 
    for w in words: 
        table = w.maketrans('', '', string.punctuation)
        w = w.translate(table).lower() 
        print(w, '\t', 1)
