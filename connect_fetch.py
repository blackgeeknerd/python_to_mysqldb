import mysql.connector
from mysql.connector import Error

#define the connector function
def connect_fetch():
    ''' function to connect and fetch rows in a database '''

    #create a variable for the connector object
    conn = None 

    try:
        conn = mysql.connector.connect(host='localhost', database='demo1', user='seyi', password='password', auth_plugin='mysql_native_password')
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

connect_fetch()