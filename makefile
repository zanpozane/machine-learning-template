IMAGE_NAME = ml-flask-app
CONTAINER_NAME = ml-flask-container
PORT = 5000

# docker
docker_build:
	docker build -t $(IMAGE_NAME) .

docker_run:
	docker run -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

docker_stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

docker_clean: stop
	docker rmi $(IMAGE_NAME)

docker_restart: stop run

docker_logs:
	docker logs -f $(CONTAINER_NAME)

# Open a shell in the running container
docker_shell:
	docker exec -it $(CONTAINER_NAME) /bin/sh

# Test the Flask API with a curl request
curl:
	sleep 5  # Give the server time to start
	curl -X POST -H "Content-Type: application/json" -d $(CURL_DATA) http://localhost:$(PORT)/predict
