build:
	docker build . -t log_output

run:
	docker run --name log_output -d log_output

logs:
	docker logs log_output

stop:
	docker stop log_output

delete_container:
	docker rm log_output

stop_and_del: stop \
	delete_container