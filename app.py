#/
#    author:   abhijayrajvansh
#    created:  16.03.2022 04:28:07
#/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By

import os
import datetime
import time

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# url to be launched ...
url = "https://dld.srmist.edu.in/srmktretelab/#/" # elab url

# Handling Chrome Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications")
# chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions)
driver.maximize_window()
# driver.minimize_window()

driver.get(url) # launches the broswer and open url

username = ""
password = ""

def login():
    driver.find_element(By.XPATH, "//input[@id='Username1']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block']").click()

login()


