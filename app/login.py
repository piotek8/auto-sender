from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv

from configuration import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        load_dotenv()

        self.username_field = "#email"
        self.password_field = "#password"
        self.next_and_login_button = "button[type='submit'] span[class='sm8uzh7']"
    def login_to_account(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        try:
            username_field = self.driver.find_element(By.CSS_SELECTOR, self.username_field)
            username_field.send_keys(email)
            next_button = self.driver.find_element(By.CSS_SELECTOR, self.next_and_login_button)
            next_button.click()

            password_field = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password_field)))
            password_field.send_keys(password)

            login_button = self.driver.find_element(By.CSS_SELECTOR, self.next_and_login_button)
            login_button.click()

        except NoSuchElementException:
            print(
                f"The item could not be found. Check IDs: {self.username_field}, {self.password_field}, {self.next_and_login_button}, {self.next_and_login_button}")
        except Exception as e:
            print(f"An error occured: {e}")



'''
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import os
from dotenv import load_dotenv


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        load_dotenv()

        self.username_field = "#email"
        self.password_field = "#password"
        self.next_and_login_button = "button[type='submit'] span[class='sm8uzh7']"

    def login(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        try:
            username_field = self.driver.find_element(By.CSS_SELECTOR, self.username_field)
            username_field.send_keys(email)
            next_button = self.driver.find_element(By.CSS_SELECTOR, self.next_and_login_button)
            next_button.click()

            password_field = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password_field)))
            password_field.send_keys(password)
            login_button = self.driver.find_element(By.CSS_SELECTOR, self.next_and_login_button)
            login_button.click()



        except NoSuchElementException:
            print(
                f"The item could not be found. Check IDs: {self.username_field}, {self.password_field}, {self.next_and_login_button}, {self.next_and_login_button}")
        except Exception as e:
            print(f"An error occured: {e}")
'''

