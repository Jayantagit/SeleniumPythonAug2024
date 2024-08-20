from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/register")
driver.maximize_window()
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=(StaleElementReferenceException,NoSuchElementException))
#subscribeCheck=driver.find_element(By.XPATH,"//input[@type='radio'][@name='newsletter'][@value='0']")
subscribeCheck=mywait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='radio'][@name='newsletter'][@value='0']")))
print(subscribeCheck.is_displayed())
print(subscribeCheck.is_enabled())
print(subscribeCheck.is_selected())
driver.close()