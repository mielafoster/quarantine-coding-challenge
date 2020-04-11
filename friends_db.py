#In this part 3 of the SQL coding challenge we will create tables in the SQLite database
#We will follow the following steps, first create a connection, then create a cursor, then create the table using execute

import sqlite3
from sqlite3 import Error

#First we will create the connection of the file
def connection(firstdb_file):
    """ create a database connection to the SQLite database
        specified by firstdb_file
    :param firstdb_file: database file
    :return: Connection object or None
    """
    connect = None
    try:
        connect = sqlite3.connect(firstdb_file)
        return connect
    #print an error if we can't connect the database
    except Error as e:
        print(e)

    return connect

#Now we're going to make some tables
def table(connect, table_sql):
    """create a table from the table_sql statement
    :param connect: Connection object
    :param table_sql: a CREATE TABLE statement
    :return:
    """
    #now we need to connect it to the cursor
    try:
        cur = connect.cursor()
        cur.execute(table_sql)
    except Error as e:
        print(e)

#Now we create the main function to create the table

def main():
    database = r"C:sqlite\db\pythonsqlite.db"
    sql1_table = """ CREATE TABLE IF NOT EXISTS
friends (
                        id integer PRIMARY KEY,
                        name text
                    ); """

    connect = connection(database)
    #NOW we create the tables
    if connect is not None:
        table(connect, sql1_table)
    else:
        print("Cannot make connection")

if __name__ == '__main__':
    main()
