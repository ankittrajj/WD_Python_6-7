import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd= 'Ankit@8285',
                database='student')

cursor = con.cursor()

age = int(input("Enter the age"))
query = "delete from detail where age={}".format(age)
cursor.execute(query)
con.commit()
print("Data deleted")