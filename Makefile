PORT=5000

dockerbuild:
	docker build -t qperformance-api .

dockerremove:
	docker container rm --force qp

dockerrun:
	docker container run --env-file ./.env -p ${PORT}:${PORT} --detach --name qp qperformance-api:latest

logs:
	docker logs --follow qp

deploy: dockerbuild dockerremove dockerrun
