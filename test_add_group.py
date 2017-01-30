# -*- coding: utf-8 -*-
import unittest
from group import Group
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="2222", header="222", footer="222"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
