#!/usr/bin/env python
# -*- coding: utf-8 -*-

import splinter, os

def test_news_of_the_world():

    with splinter.Browser(driver_name="remote",
             url="http://seleniumchrome:4444/wd/hub",
             browser="chrome") as browser:

        browser.visit("http://www.bbc.co.uk/news/world")

        assert browser.is_text_present(os.environ["TEST_SEARCH_TERM"], wait_time=20)
