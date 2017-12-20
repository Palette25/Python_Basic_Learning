#--------------------------------------------------SQLite------------------------------------------------------#
import sqlite3
flag = 0
if  open('test.db', 'r'):
    flag = 1
else:
    flag = 0
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#Build a cursor
if flag==0:
    cursor.execute('create table user (id varchar (20) primary key, name varchar (20))')
    cursor.execute('insert into user (id, name)  values (\'1\', \'Clown\')')
print(cursor.rowcount)
cursor.close()
#Close the cursor while end using it
conn.commit()
#Commit the operations
conn.close()
#Close the connection
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1', ))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

