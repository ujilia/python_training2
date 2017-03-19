from fixture.db import DbFixture
# import mysql.connector
# import pymysql.cursors

# connection with mysql.connector
db = DbFixture(host="127.0.0.1", port=3306, name="addressbook", user="root", password="root")

# connection with PyMySQL
# connection = pymysql.connect(host="127.0.0.1", port=3306, database="addressbook", user="root", password="root")

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
