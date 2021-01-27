service docker start
docker build -f Dockerfile.prod -t tmp .
docker run -it --rm -p 80:80 tmp
