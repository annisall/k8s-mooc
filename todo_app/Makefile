build:
	docker build . -t todo_app

run:
	docker run --name todo_app -d todo_app

build_and_run: build \
	run

logs:
	docker logs todo_app

stop:
	docker stop todo_app

delete_container:
	docker rm todo_app

stop_and_del: stop \
	delete_container