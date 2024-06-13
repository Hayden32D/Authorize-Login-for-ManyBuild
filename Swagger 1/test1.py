from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import json
import time
import newFileOpen


# Path to the Chrome WebDriver executable
chrome_driver_path = r'C:\webdrivers\chromedriver.exe'

# Set up Chrome WebDriver options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Uncomment this line to run in headless mode

# Create a new instance of Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the Swagger UI
    driver.get("https://wsmanybuild.azurewebsites.net/Swagger/index.html")

    # Wait for the Swagger UI element to be present
    wait = WebDriverWait(driver, 5)
    swagger_ui_element = wait.until(EC.presence_of_element_located((By.ID, "swagger-ui")))

    # Wait for the login button to be clickable
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))

    # Click the login button
    login_button.click()

    try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
    try_it_out_button.click()

    text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class*='body-param']")))

    text_to_write = '{"userName": "cmoretti+creator9@method-automation.com", "password": "Bluestone1!"}'
    text_field.clear()
    text_field.send_keys(text_to_write)

    print("Text written to the text field: ", text_to_write)

    execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
    execute_button.click()

    response_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.download-contents")))
    response_element.click()
    time.sleep(2)

    key = newFileOpen.openNewFile()
    print(key)

    authorize = driver.find_element(By.CSS_SELECTOR, "button.btn.authorize.unlocked")
    authorize.click()

    key_input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
    key_input_field.send_keys(key)

    final_press = driver.find_element(By.CSS_SELECTOR, "button.btn.modal-btn.auth.authorize.button")
    final_press.click()

    time.sleep(2)

    isLocked = driver.find_element(By.CSS_SELECTOR, "button.btn.authorize.locked")
    if(isLocked):
        print("Test was a Success! Access Granted")
    else:
        print("Authorization was not granted")

finally:
    # Ensure the browser is closed, even if an error occurs
    driver.quit()



