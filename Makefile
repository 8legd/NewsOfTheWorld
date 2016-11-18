setup:
	@sudo docker-compose build

test:
	@sudo docker-compose run tests pytest

teardown:
	@sudo docker-compose rm
