import sqlite3

conn = sqlite3.connect('accounts.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE accounts (Account_name TEXT, CSM TEXT, ES TEXT, Last_Contacted TEXT, Activity_Performed TEXT, Next_Contact TEXT )')
print("Created table successfully!")

conn.close()

