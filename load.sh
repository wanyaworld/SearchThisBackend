rm -rf books-input
mkdir books-input
for i in {2..20}
do
	wget "http://www.gutenberg.org/files/$i/$i.txt" -P books-input/
done
cd books-input
/django_static/map_reduce_static/add_name.sh
chmod 777 *
