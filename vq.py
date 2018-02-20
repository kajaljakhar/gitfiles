import sqlite3
import time

con=sqlite3.connect("newvirtualqueue.db")
c=con.cursor()


def create_table():
 c.execute("CREATE TABLE IF NOT EXISTS queue(queue_no INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,uid TEXT)")

def data_entry(name,uid):
 
 c.execute("INSERT INTO queue(name,uid) VALUES( ? ,?)",(name,uid))
 
 con.commit()
 #c.close()
 #con.close()


def input_data():
 choice=input("Want to enter data(y/n):")
 if choice=='y' or choice =='Y':
     
     name=input("Enter name :")
     uid=input("Enter uid:")
     data_entry(name,uid)
     if choice=='y' or choice=='Y':
         input_data()
         



create_table()
input_data()
c.close()
con.close()


 
 
 
