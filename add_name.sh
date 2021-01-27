for f in *.txt; do cat <(echo "$f") $f > $f.tmp && mv $f.tmp $f; done 
