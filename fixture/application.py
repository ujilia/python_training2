from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(firefox_binary=FirefoxBinary("/Applications/FirefoxESR.app/Contents/MacOS/firefox-bin"))
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8888/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
