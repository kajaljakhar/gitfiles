import sqlite3


con=sqlite3.connect("Dictionary.db")
c=con.cursor()


def find_meaning(word):
    c.execute("SELECT definition FROM entries WHERE word= '{}'".format(word))
    result=c.fetchone()
    if result!=None:
        return result
    else:
        return "No Found!"

def user_input():
    word=input("Enter a word:")
    result=find_meaning(word)
    for i in result:
        print(i)



choice='y'
while(choice=="y" or choice =="Y"):
 user_input()
 choice=input("Want to search(y/n):")

print("Thankyou")
