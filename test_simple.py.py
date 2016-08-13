from selenium import webdriver
import time

driver = webdriver.Chrome('')
driver.implicitly_wait(10)

driver.get('https://google.com')
time.sleep(10)
driver.quit()
