#!/usr/bin/env python

from selenium import webdriver
import sys

def extract_token(username, password):
    driver = webdriver.PhantomJS()
    driver.get("https://www.facebook.com")
    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(username)
    inputElement = driver.find_element_by_id("pass")
    inputElement.send_keys(password)
    inputElement.submit()
    driver.get("https://developers.facebook.com/tools/explorer/")
    return driver.find_element_by_class_name('_2toh').find_element_by_tag_name('input').get_attribute('value')

if __name__=="__main__":
    print extract_token(sys.argv[1], sys.argv[2])