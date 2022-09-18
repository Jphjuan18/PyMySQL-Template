
#from pandas_credentials import credentials 
from pandas_config import sql_conection

class MySQL:

    def create_database():
        import pymysql

        # Connect to the database
        from pandas_credentials import host,user,password, db
        cnx = pymysql.connect(host=host,
                                user=user,
                                password=password)
        # create cursor
        cursor=cnx.cursor()

        # create database
        cursor.execute("CREATE DATABASE "+db+"")
        return print(f'\n{db}l database created!')

    def create_table():
         # Connect to the database
        cursor,cnx = sql_conection() 

        from pandas_credentials import table_name, create_table
        cursor.execute(create_table)
        cnx.commit()
        return print(f'\n{table_name} table created!') 

    def insert_dataframe():
         # Connect to the database
        cursor, cnx = sql_conection()

        # Create access to pandas df
        from pandas_profile_template import read_file
        df = read_file()

        # Creating column list for insertion
        cols = "` , `".join([str(i) for i in df.columns.tolist()])

        # Insert DataFrame recrds one by one.
        from pandas_credentials import table_name
        for i,row in df.iterrows():
            sql = "INSERT INTO "+table_name+" (`" +cols+ "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"

            print(sql)
            print(tuple(row))

            cursor.execute(sql, tuple(row))
            #print(sql) 
            #print(row)   
        
            cnx.commit()
        return print('\nInserted successfully')
    
    def describe_table():
        # Connect to the database
        cursor, cnx = sql_conection() 

        from pandas_credentials import table_name
        cursor.execute("DESCRIBE "+table_name+"")
        for x in cursor:
                print(x)
        return 

    def get_server_info():
      # Connect to the database
        cursor, cnx = sql_conection() 
        
        db_Info = cnx.get_server_info()
        return print(db_Info)

    def delete_table():
        # Connect to the database
        cursor, cnx = sql_conection() 

        from pandas_credentials import table_name
        cursor.execute("DROP TABLE "+table_name+"")  
        cnx.commit()
        return print("Table "+table_name+" deleted")
    
    def delete_database():
         # Connect to the database
        cursor, cnx = sql_conection() 

        from pandas_credentials import db
        cursor.execute("DROP DATABASE "+db+"")  
        cnx.commit()
        return print("Database "+db+" deleted")
        
    def close_cnx(bool):
         # Connect to the database
        cnx = sql_conection() 
        
        if bool == True:
            cnx.close()
            return print('Connection is closed')      
        elif bool == False:
            return #print('None')   
            
    def select(query):
        # Connect to the database
        cursor, cnx = sql_conection() 
        
        cursor.execute(query)
        #for x in cursor:
        #        print(x)
        
        return cursor