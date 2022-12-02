build:
	docker build . -t log_output:$(VERSION)

run:
	docker run -p 8088:5000 --name log_output -d log_output:$(VERSION)

logs:
	docker logs log_output

stop:
	docker stop log_output

delete_container:
	docker rm log_output

stop_and_del: stop \
	delete_container