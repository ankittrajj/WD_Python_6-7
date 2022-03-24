import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd= 'Ankit@8285',
                database='student')

cursor = con.cursor()

query = "select * from detail"
cursor.execute(query)

# data = cursor.fetchone()
# data2 = cursor.fetchmany(3)
data3 = cursor.fetchall()
print(data3)
# con.commit()