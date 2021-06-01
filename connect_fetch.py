import mysql.connector as mysql
from mysql.connector import Error
import getpass

#define the connector function
def connect_fetch():
    ''' function to connect and fetch rows in a database '''

    #create a variable for the connector object
    conn = None 

    #connection parameters
    host = input('Enter Host for database')
    database = input('Enter database name')
    user = input('Enter user for database')
    password = getpass.getpass("Enter password")
    
    try: 
        conn = mysql.connect(host=host, database=database, user=user, password=password)
        print('Connecting to database server....!')
        if conn.is_connected:
            print('Connected to database server')

            #Select Query
            sql_select_query = "select * from human"
            cursor = conn.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Total number of rows in human is: ", cursor.rowcount)

            #print select output
            print("\nPrinting each Buyer record")
            for row in records:
                print("Human Id : ", row[0])
                print("Name : ", row[1])
                print("Color : ", row[2])
                print("Gender : ", row[3])
                print("Bloodgroup : ", row[4], '\n')


    except Error as e:
        print('Not connecting due to: ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown')

#call the function we just created
connect_fetch()