from TimsSurvey import survey_code, feedback_form, satisfaction_form, experience_form, order_type, order_station, \
    order_item, satisfaction_survey, likelihood_of_visit, problems_with_visit, purchase_merchandise_products, \
    beverage_order, name_of_cold_beverage, satisfaction_with_drink, satisfaction_survey_for_drink, \
    recognising_team_member, get_code, likelihood_of_repurchasing
from webdriver_setup import setup_driver
tims_url = 'https://telltims.ca/'

def main():
    surveycode= "139153302215406040642"
    driver = setup_driver(tims_url)
    driver = survey_code(driver, surveycode)
    driver = feedback_form(driver)
    driver = satisfaction_form(driver)
    driver = experience_form(driver)
    driver = order_type(driver)
    driver = order_station(driver)
    driver = order_item(driver)
    driver = satisfaction_survey(driver)
    driver = likelihood_of_visit(driver)
    driver = problems_with_visit(driver)
    driver = purchase_merchandise_products(driver)
    driver = beverage_order(driver)
    driver = name_of_cold_beverage(driver)
    driver = satisfaction_with_drink(driver)
    driver = satisfaction_survey_for_drink(driver)
    driver = likelihood_of_repurchasing(driver)
    driver = recognising_team_member(driver)
    get_code(driver, surveycode)
    driver.quit()

if __name__ == "__main__":
    main()

