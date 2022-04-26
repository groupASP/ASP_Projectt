import pymysql
import mysql.connector

connection = pymysql.connect(host="localhost", user="root", password="", database="asp_base")
conn = connection.cursor()

# conn = mysql.connector.connect(user="root", password="", host="Localhost",database="asp_base")
# curs = conn.cursor()

print(connection)