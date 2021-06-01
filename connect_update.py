import mysql.connector as mysql
from mysql.connector import Error 
import getpass
# import stdiomask



def connect_update():
    ''' function to connect and update a row in a database  '''
    
    connection = None
    num = 0
        
    #connection parameters
    host = input('Enter Host for database')
    database = input('Enter database name')
    user = input('Enter user for database') 
    password = getpass.getpass("Enter password")
    
    try: 
        connection = mysql.connect(host=host, database=database, user=user, password=password)
        cursor = connection.cursor()
        
        numEntries = int(input('Enter number'))
        
        while num < numEntries:
            #Table name
            table_name = input("Enter the table you want to update")
            #column to be changed
            column_name_to_be_changed = input("Enter the column to update")
            #New value for the column
            column_name_newValue = input("Enter the new value")
            #Id for the row
            condition_value = input("Enter the value for the condition")
            #Query
            sql_update_query = "update {} set {} = %s where id = %s" .format(table_name, column_name_to_be_changed)
            input_data = (column_name_newValue, condition_value)
            #execute the query
            cursor.execute(sql_update_query, input_data)
            #save to the database
            connection.commit()
            num += 1
            print("Record Update successfully")
            print(sql_update_query)
    except mysql.Error as e:
        print("Failed to update record to database: {}" .format(e))
    finally:
        if connection.is_connected():
            cursor.close()
            print("Database tunnel closed")
            
connect_update()
