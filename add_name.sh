for f in *.txt; do cat <(echo "$f") $f > $f.tmp && mv $f.tmp $f; done 
#for file in *.txt ; do mv $file `echo $file | sed 's/\(.*\.\)txt/\1gz/'` ; done
