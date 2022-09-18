
# DataFrame were inserting
data = '../az_grx.xlsx'

# Credentials holds the information to connect with mysql server
host='localhost'

user='root'

password=''

# Info about database
db='goodrx_drug_list'

table_name = 'drugs'

# Variables  for database
create_table = ("CREATE TABLE "+table_name+"(Drug VARCHAR(255), Pharmacy VARCHAR(255), Price INT(20))")






 # filter db name
#import re
#db_name = data.split('/')
#db_name = db_name[-1]
#db_name = db_name.split('.')
#db_name = db_name[0] 