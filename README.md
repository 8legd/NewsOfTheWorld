# News Of The World

Demo of running browser based tests in a container using [Splinter](https://splinter.readthedocs.io/en/latest/) and [Selenium](https://github.com/SeleniumHQ/docker-selenium)

The provided test case attempts to find the specified search term on the BBC World News page

## Pre-Requisites

Docker (a running docker daemon / service version 1.9 or above)

Docker compose

Git

## Usage

`git clone https://github.com/8legd/NewsOfTheWorld.git && cd NewsOfTheWorld`

`docker-compose build`

`docker-compose run -e TEST_SEARCH_TERM="<search term>" tests pytest` e.g. for success try `docker-compose run -e TEST_SEARCH_TERM="World" tests pytest`

`docker-compose stop`

`docker-compose rm -v -f`

## Debugging / Watching Tests

To view the tests as they execute you can use VNC to connect to the remote selenium environment

`vnc://localhost`

password for the VNC connection is `secret`

TIP: Use an unlikely search term e.g. `docker-compose run -e TEST_SEARCH_TERM="World Peace" tests pytest` to delay the test and give you time to connect (timeout on failure is 20 seconds)
