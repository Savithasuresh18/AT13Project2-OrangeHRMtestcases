from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32(1)\\chromedriver.exe")
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(10)
username = driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
forgot_pwrd = driver.find_element(By.XPATH,'//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]').click()
time.sleep(10)
username = driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys('Admin')
time.sleep(5)
reset_pswrd=driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(5)
success_message=driver.find_element(By.XPATH,'//p[@class="oxd-text oxd-text--p"]')
success_message_text=success_message.text
print("Success message:",success_message_text)
driver.quit()