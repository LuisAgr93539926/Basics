from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Check if we need to pick language
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Click the cookie
cookie_id = "bigCookie"
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()

time.sleep(5)