from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver_win32(1)\\chromedriver.exe")
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(10)
username = driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
password = driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('admin123')
login_button = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(10)
admin_menu = driver.find_element(By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
time.sleep(5)
menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory",
                "Maintenance", "Buzz"]
side_pane_menu =driver.find_element(By.XPATH,'//ul[@class="oxd-main-menu"]')
time.sleep(5)
actual_options = [item.text for item in side_pane_menu.find_elements(By.TAG_NAME, "li")]
time.sleep(5)
for option in menu_options:
    if option in actual_options:
        print(f"{option} menu option found")
    else:
        print(f"{option} menu option not found")
driver.quit()