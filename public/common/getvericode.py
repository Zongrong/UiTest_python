#coding=utf-8

import logging
import time
import os
from config import globalparam
from selenium import webdriver
from redis import StrictRedis,ConnectionPool
from config import globalparam


# redis = StrictRedis(host='xx.xx.xx.xx', port=6380, db=0)
dr = webdriver.Chrome(globalparam.driver_path + '/' + 'chromedriver.exe')

url = 'xxxxx'
dr.get(url)

print(dr.get_cookies())
