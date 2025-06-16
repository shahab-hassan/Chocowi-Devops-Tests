from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://35.89.148.206:3000"

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver


def test_homepage_title():
    driver = get_driver()
    driver.get(BASE_URL)
    assert "Chocowi" in driver.title
    driver.quit()


def test_login_button_exists():
    driver = get_driver()
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "signin"))
    )
    driver.quit()


def test_signup_button_exists():
    driver = get_driver()
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "signup"))
    )
    driver.quit()

def test_header_present():
    driver = get_driver()
    driver.get(BASE_URL)
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "header"))
    )
    assert header.is_displayed()
    driver.quit()


def test_search_bar_visible():
    driver = get_driver()
    driver.get(BASE_URL)
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "searchContainer"))
    )
    assert search.is_displayed()
    driver.quit()


def test_products_section_present():
    driver = get_driver()
    driver.get(BASE_URL)
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "items-container"))
    )
    assert products.is_displayed()
    driver.quit()


def test_logo_present():
    driver = get_driver()
    driver.get(BASE_URL)
    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Chocow']"))
    )
    assert logo.is_displayed()
    driver.quit()


def test_mobile_menu_button_exists():
    driver = get_driver()
    driver.set_window_size(375, 812)
    driver.get(BASE_URL)
    menu_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mobileMenuButton"))
    )
    assert menu_button.is_displayed()
    driver.quit()



def test_footer_present():
    driver = get_driver()
    driver.get(BASE_URL)
    footer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )
    assert footer.is_displayed()
    driver.quit()


def test_mobile_menu_toggle_opens_nav():
    driver = get_driver()
    driver.set_window_size(375, 812)
    driver.get(BASE_URL)

    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mobileMenuButton"))
    )
    menu_button.click()

    mobile_nav = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mobileNav"))
    )

    class_attr = mobile_nav.get_attribute("class")
    assert "active" in class_attr

    driver.quit()