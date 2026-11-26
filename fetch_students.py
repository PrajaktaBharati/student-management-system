import psycopg

conn = psycopg.connect(
    dbname="student_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT * FROM students_student")

students = cur.fetchall()

for student in students:
    print(student)

cur.close()
conn.close()