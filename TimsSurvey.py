import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Screenshot import Screenshot


def survey_code(driver, surveycode):
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'Home_iframe__T3nfU'))
    inputElement = WebDriverWait(driver, 7).until(
        EC.visibility_of_element_located((By.ID, "QR~QID9"))
    )
    inputElement.send_keys(surveycode)
    time.sleep(7)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def feedback_form(driver):
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "QID14-1-label")))
        driver.find_element(By.ID, "QID14-1-label").click()
    except selenium.common.exceptions.TimeoutException:
        print("Loading took too much time!")
    except selenium.common.exceptions.NoSuchWindowException:
        print("The browser window was closed unexpectedly.")
    except selenium.common.exceptions.WebDriverException as e:
        print(f"WebDriverException occurred: {e}")
    finally:
        if driver:
            driver.quit()

def satisfaction_form(driver):
    time.sleep(7)
    driver.find_element(By.ID, "QID15-4-label").click()
    time.sleep(7)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def experience_form(driver):
    time.sleep(7)
    driver.find_element(By.ID, "QR~QID45").send_keys("Beverage")
    time.sleep(7)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def order_type(driver):
    time.sleep(7)
    driver.find_element(By.ID, "QID18-5-label").click()
    time.sleep(7)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def order_station(driver):
    time.sleep(7)
    driver.find_element(By.ID, "QID19-5-label").click()
    time.sleep(7)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def order_item(driver):
    time.sleep(7)
    driver.find_element(By.ID, "QID20-5-label").click()
    time.sleep(7)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def satisfaction_survey(driver):
    time.sleep(7)
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID23~4~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID23~6~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID23~7~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID23~8~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID23~10~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID23~11~1\"]").click()
    driver.find_element(By.ID, "NextButton").click()
    time.sleep(15)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def likelihood_of_visit(driver):
    time.sleep(7)
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID44~1~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID44~3~1\"]").click()
    driver.find_element(By.ID, "NextButton").click()
    return driver

def problems_with_visit(driver):
    time.sleep(7)
    driver.find_element(By.ID, "QID37-2-label").click()
    driver.find_element(By.ID, "NextButton").click()
    return driver

def purchase_merchandise_products(driver):
    time.sleep(7)
    driver.find_element(By.ID, "QID134-2-label").click()
    driver.find_element(By.ID, "NextButton").click()
    return driver

def beverage_order(driver):
    time.sleep(7)
    try:
        driver.find_element(By.XPATH, "//*[@id='QID48-4-label']").click()
    except:
        print("element not found")
    driver.find_element(By.ID, "NextButton").click()
    return driver

def name_of_cold_beverage(driver):
    time.sleep(7)
    driver.find_element(By.XPATH, "//*[@id='QID54-108-label']").click()
    driver.find_element(By.ID, "NextButton").click()
    return driver

def satisfaction_with_drink(driver):
    time.sleep(7)
    driver.find_element(By.XPATH, "//*[@id='QID57-1-label']").click()
    driver.find_element(By.ID, "NextButton").click()
    return driver

def satisfaction_survey_for_drink(driver):
    time.sleep(7)
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~8~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~9~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~10~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~1~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~2~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~3~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~6~1\"]").click()
    driver.find_element(By.CSS_SELECTOR, "label[for=\"QR~QID59~7~1\"]").click()
    driver.find_element(By.ID, "NextButton").click()
    return driver

def likelihood_of_repurchasing(driver):
    time.sleep(7)
    driver.find_element(By.XPATH, "//*[@id='QID74-4-label']").click()
    time.sleep(7)
    driver.find_element(By.ID, "NextButton").click()
    return driver

def recognising_team_member(driver):
    time.sleep(7)
    driver.find_element(By.XPATH, "//*[@id='QID68-2-label']").click()
    driver.find_element(By.ID, "NextButton").click()
    return driver

def get_code(driver, surveycode):
    time.sleep(7)
    driver.find_element(By.XPATH, "//*[@id='EndOfSurvey']/strong[1]").text
    ss = Screenshot.Screenshot()
    screen_shot = ss.full_screenshot(driver, save_path= r'.', image_name = surveycode+'.png')
    print(screen_shot)









