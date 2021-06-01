import mysql.connector as mysql
from mysql.connector import Error
import getpass

def connect_insert():
    ''' function to connect and insert a row in a database  '''

    #create a connection variable
    conn = None
    
    #connection parameters
    host = input('Enter Host for database')
    database = input('Enter database name')
    user = input('Enter user for database')
    password = getpass.getpass("Enter password")
    
    try:
        conn = mysql.connect(host=host, database=database, user=user, password=password)
        # conn = mysql.connector.connect(host='localhost', database='demo1', user='#', password='#', auth_plugin='mysql_native_password')
        print('Connecting to database')
        if conn.is_connected:
            print('Connected to the database')
            db_cursor = conn.cursor()

            #create a variable to contain the sql query to be excecuted
            sql = "INSERT INTO Human (humanId, name, color, sex, Bloodgroup) VALUES (%s, %s, %s, %s, %s)"
           
           #create a list variable to contain all the values we want to insert into the database
            val = [
                    ('1008', 'Hannah', 'White', 'Female', 'B-'),
                    ('1009', 'Michael', 'Brown', 'Male', 'O-'),
                    ('1010', 'Sandy', 'Black', 'Male', 'O+'),
                    ('1011', 'Green', 'Yellow', 'Male', 'AB'),
                    ('1012', 'Richard', 'Black', 'Male', 'B+')
                ]

            #execute the query using the executemany function    
            db_cursor.executemany(sql, val)

            #commit to the database
            conn.commit()

            #print a success message
            print(db_cursor.rowcount, "rows was inserted.")
            
            #close the cursor
            db_cursor.close
            
    except Error as e:
        print('Connection failed due to the following :', e)
    finally:
        if conn is not None and conn.is_connected:
            conn.close
            print('Disconnected from database')

#call the function we just created
connect_insert()

