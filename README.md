# News Of The World

Demo of running browser based tests in a container using [Splinter](https://splinter.readthedocs.io/en/latest/) and [Selenium](https://github.com/SeleniumHQ/docker-selenium)

The provided test case attempts to find the specified search term on the BBC World News page

## Pre-Requisites

Docker (a running docker daemon / service version 1.9 or above)

Docker compose

Make & Git

## Usage

`git clone https://github.com/8legd/NewsOfTheWorld.git && cd NewsOfTheWorld`

`make setup`

`make test sch=<search term>` e.g. for success try `make test sch="World"`

`make teardown`

## Debugging / Watching Tests

To view the tests as they execute you can use VNC to connect to the remote selenium environment

`vnc://localhost`

password for the VNC connection is `secret`

TIP: Use an unlikely search term e.g. `make test sch="World Peace"` to delay the test and give you time to connect (timeout on failure is 20 seconds)
