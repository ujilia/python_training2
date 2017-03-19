# from fixture.db import DbFixture
# import mysql.connector
# import pymysql.cursors
from fixture.orm import ORMFixture

# connection with mysql.connector
# db = DbFixture(host="127.0.0.1", port=3306, name="addressbook", user="root", password="root")

# connection with PyMySQL
# connection = pymysql.connect(host="127.0.0.1", port=3306, database="addressbook", user="root", password="root")

# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()


db = ORMFixture(host="127.0.0.1", port=3306, name="addressbook", user="root", password="root")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()

