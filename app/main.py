from configuration import ConfigurationManager
from login import LoginPage
from home import HomePage
from app.setup import Setup

def main():
    config_manager = ConfigurationManager()
    driver = config_manager.get_driver_and_open_web()

    login_page = LoginPage(driver)
    login_page.login_to_account()

    home_page = HomePage(driver)
    home_page.navigate_home()

    setup = Setup(driver)  # Tworzymy instancję klasy Setup
    setup.click_technologies(driver)

if __name__ == "__main__":
    main()
