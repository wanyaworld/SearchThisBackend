for f in books-input/*.txt; do cat $f | ./mapper.py $1 | ./reducer.py; done 
#for f in books-input/*.txt; do cat <(echo "$f") $f > $f.tmp && mv $f.tmp $f; done 
