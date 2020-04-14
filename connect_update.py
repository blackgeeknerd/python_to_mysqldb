import mysql.connector as mysql
from mysql.connector import Error

#1 - Connect and update a row, hard-coded values
def connect_update():
    ''' function to connect and update a row in a database  '''
    
    conn = None

    try:
        #connect to the database using the connect function in line 12
        conn = mysql.connect(host='localhost', 
        #remember database should be the database you accessing
        database='demo1', 
        # the user should be the user in your mysql workbench      
        user='seyi', 
        #the password should be the password to the user in line 15        
        password='password',    
        auth_plugin='mysql_native_password')
        #display connecting message
        print('Connecting to database')

        if conn.is_connected:
            print('Connected to the database')
            db_cursor = conn.cursor()

            #Check dataset before updating a row

            print("Before Updating a record")
            #Create a query variable to select the row we want to update
            sql_query = 'select * from human where humanId = 1006' #remember the id 1006 must exist before we can update it

            #execute query using the execute function
            db_cursor.execute(sql_query)

            #create a variable to fetch a record from the executed query in line 31
            record = db_cursor.fetchone()
            print(record)

            #Now we can proceed to updating the row
            #Create a query variable
            sql_query_update = "update human set Sex = 'Female' where humanId = 1006"
            #execute the query variable we created in line 36 by using the execute function in line 38
            db_cursor.execute(sql_query_update)

            #commit the executed query into the database
            conn.commit()
            #display a success message
            print('record Updated Successfully')

    except Error as e:
        print('Connection failed due to the following :', e)
    finally:
        if conn is not None and conn.is_connected:
            conn.close
            print('Disconnected from database')


connect_update()
