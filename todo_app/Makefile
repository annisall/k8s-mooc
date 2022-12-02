build:
	docker build . -t todo_app:$(VERSION)

run:
	docker run -p 8088:5000 --name todo_app -d todo_app:$(VERSION)

build_and_run: build $(VERSION) \
	run $(VERSION)

logs:
	docker logs todo_app

stop:
	docker stop todo_app

delete_container:
	docker rm todo_app

stop_and_del: stop \
	delete_container