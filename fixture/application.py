from fixture.contact import ContactHelper
from fixture.group import GroupHelper

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1:8080/addressbook/")

    def destroy(self):
        self.wd.quit()