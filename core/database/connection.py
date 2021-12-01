import psycopg2


class MyDb:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="mydb", user='postgres', password='localHost123', host='localhost', port='5432')
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def createTable(self):
        sql = '''Create  Into mydb'''
        self.cursor.execute(sql)
        self.conn.close()
