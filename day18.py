# data bases

import sqlite3  # file based databased

connection = sqlite3.connect("student.db")

_cursor = connection.cursor()
try:
 _cursor.execute("create table student (name,roll_no,grade)")
except sqlite3.OperationalError as e:
    
    pass
# _cursor.execute("insert into student values ('ram',20,21)")

# connection.commit()

result= _cursor.execute("select name from student")
print(result)
for a in result:
    print(a)