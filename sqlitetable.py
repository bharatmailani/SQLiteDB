import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
        Create table student(
        student_id INT AUTO INCREMENT PRIMARY KEY,
        student_Name VARCHAR(50),
        student_class VARCHAR(10),
        student_email VARCHAR(30)
        )
    ''')
conn.close()
