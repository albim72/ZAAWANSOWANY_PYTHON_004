import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()
db.autocommit = True
tablestudent = "CREATE TABLE IF NOT EXISTS student(imie VARCHAR(50),nazwisko VARCHAR(50),student_id int primary key);"

cursorObject.execute(tablestudent)

sql = "INSERT INTO student(imie,nazwisko,student_id) VALUES(%s,%s,%s)"
val = ("Jan","Kos",655662)

cursorObject.execute(sql,val)
#db.commit()

many = [
    ("Olga","Nowak",65565),
    ("Olek","Nowak",6732),
    ("Paweł","Nowak",756756),
    ("Olga","Kos",655835365),
    ("Tomek","Nowik",655676565),
    ("Henio","Nowak",6557565),
    ("Nadia","Nowak",657565),
]

cursorObject.executemany(sql,many)
db.close()
