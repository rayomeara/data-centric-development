import os
import datetime
import pymysql

# Get username from workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    '''
    # Select
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
    '''
    '''
    # Create table
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
    '''
    '''
    # Insert
    with connection.cursor() as cursor:
        #row = ("Bob", 21, "1990-02-06 23:04:56")
        #cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
               ("Jim", 56, "1955-05-09 12:12:45"),
               ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
    '''
    '''
    # Update
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                        (23, 'Bob'))
        connection.commit()
    '''
    '''
    # Update
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                        rows)
        connection.commit()
    '''

    # Delete
    with connection.cursor() as cursor:
        #cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        #connection.commit()
        #cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob')
        #connection.commit()
        #cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim'])
        #connection.commit()
        #cursor.executemany("DELETE FROM Friends WHERE name IN ('Jim','Bob');")
        #connection.commit()
        list_of_names = ['Fred', 'fred']
        # Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name IN ({});".format(format_strings), list_of_names)
        connection.commit()


finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
