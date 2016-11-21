#!/usr/bin/env python
# -*- coding: utf-8 -*-

import splinter, os, urllib2, time

def test_news_of_the_world():

    # if needed wait a few seconds for the driver to be up and running - sometimes takes a while on first load
    driver_url = "http://seleniumchrome:4444/wd/hub"
    req = urllib2.Request(driver_url)
    try: urllib2.urlopen(req)
    except urllib2.URLError as e:
        time.sleep(10)

    with splinter.Browser(driver_name="remote",
             url=driver_url,
             browser="chrome") as browser:

        browser.visit("http://www.bbc.co.uk/news/world")

        assert browser.is_text_present(os.environ["TEST_SEARCH_TERM"], wait_time=20)
