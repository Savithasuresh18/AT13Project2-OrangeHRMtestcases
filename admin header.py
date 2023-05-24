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
page_title = driver.title
expected_title = "OrangeHRM"
assert page_title == expected_title, f"Page title should be '{expected_title}', but it is '{page_title}'."
time.sleep(5)
admin_menu = driver.find_element(By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').click()
time.sleep(5)
expected_headers = ["User management", "Job", "Organisation", "Qualification", "Nationalities", "Corporate Banking", "Configuration"]
admin_headers = driver.find_elements(By.CSS_SELECTOR, "div#content div.head h1")
time.sleep(5)
for header in admin_headers:
    header_text = header.text
    assert header_text in expected_headers, f"Header '{header_text}' is missing."
time.sleep(5)
print("Title and Header validation on the Admin page passed successfully.")
driver.quit()