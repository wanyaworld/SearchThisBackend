mkdir map_reduce_static
cp ../singe_run.sh ./map_reduce_static -r
cp ../load.sh ./map_reduce_static -r
cp ../deinit.sh ./map_reduce_static -r
cp ../add_name.sh ./map_reduce_static -r
cp ../single_run.sh ./map_reduce_static -r
cp ../mapper.py ./map_reduce_static -r
cp ../reducer.py ./map_reduce_static -r

service docker start
docker build -f Dockerfile.prod -t tmp_back .
docker run -it --rm -p 80:80 tmp_back
