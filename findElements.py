from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
driver.maximize_window()
driver.implicitly_wait(5)
optionList=driver.find_elements(By.CSS_SELECTOR,"div.list-group a")
print(type(optionList))
print(len(optionList))
for ele in optionList:
    print(ele.text)
driver.close()
