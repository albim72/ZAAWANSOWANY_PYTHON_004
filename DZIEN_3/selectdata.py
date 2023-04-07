import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()
#db.autocommit = True
query = "SELECT * FROM student WHERE student_id > 100000;"
cursorObject.execute(query)

wynik = cursorObject.fetchall()

for x,y,z in wynik:
    print(f'ID: {z}, imię: {x}, nazwisko: {y}')

db.close()
