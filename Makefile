setup:
	@sudo docker-compose build

test:
	@sudo docker-compose run -e TEST_SEARCH_TERM="$(sch)" tests pytest

teardown:
	@sudo docker-compose stop
	@sudo docker-compose rm -v -f
