import sqlite3
import time

con=sqlite3.connect("virtualqueue.db")
c=con.cursor()
def get_data():
    c.execute("SELECT * FROM queue")
    
    for i in c.fetchall():
        print(i)

get_data()
print (time.strftime("%H:%M  %d-%m-%Y"))
