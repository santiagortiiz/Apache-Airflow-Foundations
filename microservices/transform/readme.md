docker build -t <tag>:<version> <build_context_path>
docker build -t transform .

docker run --name <container_name> -d -p <host_port>:<container_prot> <image_name>
docker run --rm --name transform -d -p 8002:80 --network etl transform