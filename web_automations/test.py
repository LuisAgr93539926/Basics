from selenium import webdriver
import time


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    time.sleep(5)
    print(driver.title)
