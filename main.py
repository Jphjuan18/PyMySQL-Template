#from pandas_credentials import data,db_name


#from pandas_profile_template import read_file
#q1 = read_file()
#print(q1)
#print(q1.info())

#print(q1.isna().sum())


import pandas_sqlcnx
#pandas_sqlcnx.MySQL.create_database()
#pandas_sqlcnx.MySQL.delete_table()

#pandas_sqlcnx.MySQL.create_table()
#pandas_sqlcnx.MySQL.describe_table()


#pandas_sqlcnx.MySQL.insert_dataframe()



#from pandas_credentials import db_name
#pandas_sqlcnx.MySQL.delete_database()

#query = 'SELECT State FROM acutecare WHERE DISEASES = "Any condition" LIMIT 5000,7632'

#query = 'SELECT  State, SUM(AcuteCareService) AS AcuteCareService FROM acutecare GROUP BY State'

#q2 = 'SELECT State, AcuteCareService, SUM(ServiceCount) AS ServiceCount FROM acutecare GROUP BY State, AcuteCareService ORDER BY `ServiceCount` asc'



#s1 = pandas_sqlcnx.MySQL.select(query)

#print(type(s1))
#print(s1)