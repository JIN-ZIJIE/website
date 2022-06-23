import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd= '123456')

my_cursor = mydb.cursor()


# my_cursor.execute("CREATE DATABASE 问题")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
