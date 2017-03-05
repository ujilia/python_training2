import mysql.connector

class DbFixture:
    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, port=port, database=name, user=user, password=password)

    def destroy(self):
        self.connection.close()