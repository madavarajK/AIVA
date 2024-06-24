import sqlite3


conn = sqlite3.connect('aiva.db')
mycursor=conn.cursor()
    
temp=mycursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
    
for row in temp:
    print(row)