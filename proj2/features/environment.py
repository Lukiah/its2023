#!/usr/bin/env python3
# 
# VUT FIT - ITS 2022/2023 Projekt 2
# Lukáš Zedek (xzedek03)
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def before_all(context):
    time.sleep(1)
    context.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    context.driver.implicitly_wait(15)
    context.base_url = "http://mys01.fit.vutbr.cz:8090/"

def after_all(context):
    time.sleep(1)
    context.driver.quit()