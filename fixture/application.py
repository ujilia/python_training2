from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(firefox_binary=FirefoxBinary("/Applications/FirefoxESR.app/Contents/MacOS/firefox-bin"))
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8888/addressbook/index.php")

    def create_group(self, group):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill in group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to home page
        wd.find_element_by_link_text("group page").click()

    def destroy(self):
        self.wd.quit()
