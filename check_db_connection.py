import mysql.connector
# import pymysql.cursors

# connection with mysql.connector
connection = mysql.connector.connect(host="127.0.0.1", port=3306, database="addressbook", user="root", password="root")

# connection with PyMySQL
# connection = pymysql.connect(host="127.0.0.1", port=3306, database="addressbook", user="root", password="root")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
