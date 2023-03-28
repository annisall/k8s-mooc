build:
	docker build . -t pingpong:$(VERSION)

run:
	docker run -p 8088:5000 --name pingpong -d pingpong:$(VERSION)

logs:
	docker logs pingpong

stop:
	docker stop pingpong

delete_container:
	docker rm pingpong

stop_and_del: stop \
	delete_container