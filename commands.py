import time

from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://www.ebay.com/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
#print(driver.page_source)
driver.switch_to.new_window("tab")
driver.get("https://www.amazon.com/")

time.sleep(5)
driver.close()