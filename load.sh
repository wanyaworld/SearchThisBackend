for i in {2..20}
do
	wget "http://www.gutenberg.org/files/$i/$i.txt" -P books-input/
done
