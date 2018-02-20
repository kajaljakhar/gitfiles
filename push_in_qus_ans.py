import sqlite3

con1=sqlite3.connect('Dictionary.db')
c=con1.cursor()


c.execute("SELECT word FROM entries LIMIT 10")
qus=c.fetchone()
print(qus)

c.execute("SELECT definition FROM entries LIMIT 10")
ans=c.fetchone()
print(ans)

con2=sqlite3.connect("qu")
c1=con2.cursor()
c1.execute("CREATE TABLE if not exists trh(w varchar,d varchar)")

#c1.execute("SELECT * FROM qa")
#result=c1.fetchall()
#for r in result:
#    print (r)
c1.execute("INSERT into trh values('{}','{}')".format(qus,ans))
c1.execute("select * from tr")
print(c1.fetchall())

