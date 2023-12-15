from selenium.webdriver.common.by import By

from app.configuration import BasePage

from app.dictonaries import TECHNOLOGY_DICT
from constants import TECHNOLOGY
class Setup(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.search_field = "div[data-test='dropdown-element-kw'] input[type='text']" #css
        self.junior_position_field = "(//*[name()='svg'])[50]" #xpath
        self.publication_time_24h = "(//*[name()='svg'])[72]" #xpath
        self.show_offer_button = "div[class='core_s1cjjpc4'] button[class='size-large variant-primary core_b1fqykql']" #css

    def click_technologies(self, driver):
        for tech in TECHNOLOGY:
            if tech in TECHNOLOGY_DICT.values():
                xpath = f"//div[contains(text(), '{tech}')]"
                element = driver.find_element(By.XPATH, xpath)
                element.click()
'''
    def navigate_home(self):
        try:
            search_button = self.driver.find_element(By.CSS_SELECTOR, self.search_field)
            search_button.click()


            accept_cookies = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_field)))
            accept_cookies.click() if accept_cookies else None

            go_to_homepage_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.home_page)))
            go_to_homepage_button.click()

            search_button = self.driver.find_element(By.CSS_SELECTOR, self.search)
            search_button.click()

        except NoSuchElementException:
            print(f"The item could not be found. Check selectors: {self.cookies}, {self.home_page}, {self.search}")
        except Exception as e:
            print(f"An error occured: {e}")
'''