import selenium
from selenium import webdriver
from pathlib import Path
import os

myOutputPath = Path(__file__).parents[0]
geckodriverPath = f"(myPath)/geckodriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME, 'q').send_keys('Bauer')
