docker build -t <tag>:<version> <build_context_path>
docker build -t load .

docker run --name <container_name> -d -p <host_port>:<container_prot> <image_name>
docker run --rm --name load -d -p 8003:80 --network etl load