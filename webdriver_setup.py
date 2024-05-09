import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_experimental_option("detach", True)

chromedriver_path = 'C:/Users/Utkarsha Kahalekar/OneDrive/Desktop/chromedriver-win64/chromedriver.exe'

def setup_driver(tims_url):
    driver = webdriver.Chrome(options=option)
    driver.get(tims_url)
    return driver

