import psycopg2


class MyDb:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="db_todo", user='postgres', password='localHost123', host='localhost', port='5432')
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def createTable(self):
        sql = '''Create  Into mydb'''
        self.cursor.execute(sql)
        self.conn.close()
        
    def post(self,query:str ):
        print(query)
        self.cursor.execute(query)
        self.conn.close()
        
    def get(self,query:str ):
        print(query)
        self.cursor.execute(query)
        #self.conn.close()
        return self.cursor.fetchall()
        
