import sqlite3

con=sqlite3.connect("exp.txt")
c=con.cursor()

c.execute("create table qa(n text)")
c.execute("insert into qa values('hello')")
