docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
docker rmi -f $(docker images -a -q)