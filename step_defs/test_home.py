import logging
import os

from pytest_bdd import scenario, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

feature_file_path = os.path.abspath('features/home.feature')


@scenario(feature_file_path, 'Check Home Page')
def test_publish():
    pass


@given('Make sure the browser is open')
def step_impl():
    logging.info("Browser is opened")


@when('Access the home page')
def step_impl(browser):
    browser.get('https://www.google.com/')


@then('All page resources will be loaded')
def step_impl(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    browser.find_element(By.NAME, 'q')
