import sqlite3

conn = sqlite3.connect('sr.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE srvreq (ID INTEGER PRIMARY KEY, Account_name TEXT, Customer_name TEXT, SR_Last_Conducted DATE, ES_Account TEXT, SR_Next_Schedule DATE)')
print("Created table successfully!")

conn.close()

