import sqlite3
import json
from datetime import datetime

sql_transaction=[]
timeframe="2016-11"
con=sqlite3.connect("{}.db".format(timeframe))

c=con.cursor()

def format_data(data):
    data=data.replace("\n"," ").replace("\t"," ").replace('"',"'")
    return data


def find_parent(pid):
    sql="SELECT comment FROM parent_reply WHERE comment_id= '{}' LIMIT 1".format(pid)
    c.execute(sql)
    result=c.fetchone()
    if result!= None:
        return result[0]
    else:
        return False

    
def find_exists_parent(pid):
    c.execute("SELECT score FROM parent_reply WHERE parent_id= '{}' LIMIT 1".format(pid))
    result = c.fetchone()
    if result!= None:
        return result[0]
    else:
        return False
        
def acceptable(data):
    if len(data.split(' '))>50 or len(data.split(' '))<1:
        return False
    elif len(data)>1000:
        return False
    elif data=='[deleted]' or data=='[removed]':
        return False
    else:
        return True
    



def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT ,comment_id TEXT ,parent TEXT,comment TEXT,subreddit TEXT,unix INT,score INT)")
    

if __name__=="__main__":
    create_table()
    row_counter=0
    row_pair=0
    with open("/home/karan/RC_2006-11",buffering=1000) as f:
        for row in f:
            row_counter +=1
            row=json.loads(row)
            parent_id=row["parent_id"]
            created_utc=row["created_utc"]
            subreddit=row["subreddit"]
            score=row["score"]
            comment_id=row["link_id"]
            body=format_data(row["body"])
            parent_data=find_parent(parent_id)
            if score>=2:
                if acceptable(body):
                    exists_parent_score=find_exists_parent(parent_id)
                    if exists_parent_score:
                        if exists_parent_score>score:

                            c.execute("UPDATE parent_reply SET parent_id = ?,comment_id = ?,comment = ?,subreddit = ?,unix = ?,score = ? WHERE parent_id= ?",(parent_id,comment_id,body,subreddit,created_utc,score,parent_id))
                            
                            con.commit()
                    elif parent_data:        
                            c.execute("INSERT INTO parent_reply(parent_id,comment_id,parent,comment,subreddit,unix,score) VALUES (?,?,?,?,?,?,?)",(parent_id,comment_id,parent_data,body,subreddit,created_utc,score))
                            row_pair +=1
                            
                            con.commit()
                            
                    else:
                            c.execute("INSERT INTO parent_reply(parent_id,comment_id,comment,subreddit,unix,score) VALUES (?,?,?,?,?,?)",(parent_id,comment_id,body,subreddit,created_utc,score))
                            
                            
                            con.commit()
                            



            if row_counter%1000==0:
                print("row=",row_counter,"pair=",row_pair)
             
