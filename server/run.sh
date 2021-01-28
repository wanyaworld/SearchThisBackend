service docker start
docker build -f Dockerfile.prod -t tmp_back .
docker run -it --rm -p 81:81 tmp_back
