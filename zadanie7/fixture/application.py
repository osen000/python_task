from selenium.webdriver.firefox.webdriver import WebDriver
from zadanie7.fixture.contact import ContactHelper
from zadanie7.fixture.group import GroupHelper
from zadanie7.fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1:8080/addressbook/")

    def destroy(self):
        self.wd.quit()