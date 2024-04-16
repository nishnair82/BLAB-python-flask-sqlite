import sqlite3

conn = sqlite3.connect('accounts.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE accounts (ID INTEGER PRIMARY KEY, Account_name TEXT, CSM TEXT, ES TEXT, Last_Contacted DATE, Activity_Performed TEXT, Next_Contact DATE )')
print("Created table successfully!")

conn.close()

