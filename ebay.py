from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://www.ebay.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for anything']").send_keys("Laptop")
driver.find_element(By.CSS_SELECTOR,"#gh-btn").click()