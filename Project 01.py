import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
import time
driver_path = r"E:\Automation testing\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

####Test case ID:TC_login_01
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

username=driver.find_element(By.XPATH,'//input[@placeholder="Username"]')
username.send_keys("Admin")

password=driver.find_element(By.XPATH,'//input[@placeholder="Password"]')
password.send_keys("admin123")

login=driver.find_element(By.XPATH,'//button[@type="submit"]')
login.click()

###Test case ID:TC_login_02
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

username=driver.find_element(By.XPATH,'//input[@placeholder="Username"]')
username.send_keys("Admin")

password=driver.find_element(By.XPATH,'//input[@placeholder="Password"]')
password.send_keys("invalid password")

login=driver.find_element(By.XPATH,'//button[@type="submit"]')
login.click()

#fetching the error message for invalid logins from web page
print(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p').text)

#Test case ID:TC_PIM_01
pim=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span").click()
time.sleep(1)

add=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(1)

firstname=driver.find_element(By.XPATH,'//input[@placeholder="First Name"]')
time.sleep(1)
firstname.send_keys("Arul")

middlename=driver.find_element(By.XPATH,'//input[@placeholder="Middle Name"]')
time.sleep(1)
middlename.send_keys("Raja")

lastname=driver.find_element(By.XPATH,'//input[@placeholder="Last Name"]')
time.sleep(1)
lastname.send_keys("R")

employeeid=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
time.sleep(1)
employeeid.send_keys("3215")

photo=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/div/img').click()
time.sleep(2)
pyautogui.write("E:\Automation testing\orchid_flower_1.jpg")
time.sleep(2)
pyautogui.press('enter')
time.sleep(1)

save1=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(2)

# ###Test case ID:TC_PIM_02
pim1=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span").click()
time.sleep(2)

edit=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i').click()
time.sleep(2)

otherid=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
time.sleep(2)
otherid.send_keys("DFG586321")

drivelicense=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
time.sleep(1)
drivelicense.send_keys("XXX585821")
time.sleep(2)

gender=driver.find_element(By.XPATH,'//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"]').click()
time.sleep(3)

save=driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')
save.click()
time.sleep(2)

# ###Test case ID:TC_PIM_03
pim2=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span").click()
time.sleep(2)

delete=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[2]/i').click()
time.sleep(2)
popup_link = driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click()
whandle=driver.window_handles[0]
driver.switch_to.window(whandle)
time.sleep(3)

