import mysql.connector

mydb = mysql.connector.connect(host="localhost",user='root',passwd='root',database='world')

mycursor = mydb.cursor()

mycursor.execute("select * from world.country")

result = mycursor.fetchmany(10)
for entry in result:
    print(entry)
