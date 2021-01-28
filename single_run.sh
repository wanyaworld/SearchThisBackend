for f in /django_static/books-input/*.txt; do cat $f | /django_static/map_reduce_static/mapper.py $1 | /django_static/map_reduce_static/reducer.py; done 
#for f in books-input/*.txt; do cat <(echo "$f") $f > $f.tmp && mv $f.tmp $f; done 
