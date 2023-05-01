docker build -t <tag>:<version> <build_context_path>
docker build -t etl .

docker run --name <container_name> -d -p <host_port>:<container_prot> <image_name>
docker run --rm --name etl -d -p 8004:80 --network etl etl