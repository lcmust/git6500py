#!/usr/bin/env python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## from django.test import LiveServerTestCase

## class AdminTest(LiveServerTestCase):
##     def setUp(self):
##         self.browser = webdriver.Firefox()

##     def tearDown(self):
##         self.browser.quit()

##     def test_admin_site(self):
##         self.browser.get(self.live_server_url + '/admin/')
##         body = self.browser.find_element_by_tag_name('body')
##         self.assertIn('Django administration', body.text)
browser = webdriver.Firefox()
browser.get("http://www.oschina.net")
