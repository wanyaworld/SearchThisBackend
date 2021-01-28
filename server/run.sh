service docker start
docker build -f Dockerfile.prod -t tmp_back .
docker run -it --rm -p 80:80 tmp_back
