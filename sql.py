
#This is a 2 part project day8 and day9. For day8 I learned SQL language and then I executed the code in python with the sqlite3 package
#We will use python to write code in sqlite3

import sqlite3

#now we need to create a connection to pass the name of the databse you want to access
#then we will create an object that is called to be capable to send commands to the sqlite3#The cursor will allow us to fetch records of  the database
#then we create a table in the database

connect_db = sqlite3.connect("firstdb.db")

cursor = connection.cursor()

#Now we can create a table in the database
sql_com = """ CREATE TABLE emp (fname VARCHAR(20), lname VARCHAR(30));"""
#indidcates that it can only be 20 or 30 characters

cursor.execute(sql_com)
#now we will execute the statement

#Now we can attempt to insert data into the table
sql2_com = """ INSERT INTO emp VALUES("Miela", "Foster"); """
cursor.execute(sql2_com)

#Its important that before we close our connection we save the changes in the file we jsut created
connection.commit()
connection.close()
