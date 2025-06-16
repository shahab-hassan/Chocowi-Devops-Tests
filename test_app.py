from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

def test_homepage_title():
    driver = get_driver()
    driver.get("http://35.89.148.206:3000/")
    assert "Chocowi" in driver.title
    driver.quit()

def test_login_button_exists():
    driver = get_driver()
    driver.get("http://35.89.148.206:3000/")
    time.sleep(2)
    assert driver.find_element(By.CLASS_NAME, "signin")
    driver.quit()