docker build -t <tag>:<version> <build_context_path>
docker build -t extract .

# Development
uvicorn extract:app --reload

# Production
docker run --rm --name <container_name> -d -p <host_port>:<container_prot> <image_name>
docker run --rm --name extract -d -p 8001:80 --network etl extract