from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"[name='username']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"[name='password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
print(driver.title)
assert driver.title=="OrangeHRM"
driver.find_element(By.XPATH,"//a[contains(@href,'leave')]").click()
driver.close()