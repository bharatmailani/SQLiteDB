import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    insert into student (student_name,student_class,student_email) VALUES('RAM','10TH','ram@gmail.com'),('DEEPAK','12th','deepak@gmail.com')

'''
conn.execute(ins)
conn.commit()
conn.close()