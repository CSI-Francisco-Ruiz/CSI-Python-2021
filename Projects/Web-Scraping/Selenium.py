import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.options import Options

myOutputPath = Path(__file__).parents[0]
geckodriverPath = f"(myPath)/geckodriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME, 'q').send_keys('Discord mod')