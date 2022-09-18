

def sql_conection():
    import pymysql

     # Connect to the database
    from pandas_credentials import host,user,password,db
    cnx = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                db=db)
    # create cursor
    cursor=cnx.cursor()
    return cursor, cnx