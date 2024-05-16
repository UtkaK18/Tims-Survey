import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Create ChromeOptions
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_experimental_option("detach", True)

# Create DesiredCapabilities
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True
capabilities['pageLoadStrategy'] = 'normal'
capabilities['timeouts'] = { 'implicit': 10, 'pageLoad': 30, 'script': 30 }
capabilities['goog:loggingPrefs'] = { 'browser': 'ALL', 'driver': 'ALL' }

# Merge Options and Capabilities
for key, value in capabilities.items():
    option.set_capability(key, value)

chromedriver_path = 'C:/Users/Utkarsha Kahalekar/OneDrive/Desktop/chromedriver-win64/chromedriver.exe'

def setup_driver(tims_url):
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=option)
    driver.set_page_load_timeout(60)
    driver.get(tims_url)
    return driver