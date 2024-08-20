from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#Single single checkbox
#driver.find_element(By.ID,"sunday").click()
# Multi checkbox
daysCheckboxList=driver.find_elements(By.XPATH,"//label[@for='days']/parent::div//input")
daysCount=len(daysCheckboxList)
print(daysCount)
'''
for day in range(0,daysCount):
    daysCheckboxList[day].click()
'''
# Chekboxes on Choice
for day in daysCheckboxList:
   id= day.get_attribute("id")
   if id=="monday" or id=="friday":
       day.click()

femaleGender=driver.find_element(By.ID,"female")
if not femaleGender.is_selected():
    femaleGender.click()
