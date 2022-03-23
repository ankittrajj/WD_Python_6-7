import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd = 'Ankit@8285',
                database = 'emp')

# if con.is_connected():
#     print("Connection successfully!!")

cursor = con.cursor()

name = input("Enter the name")
age = int(input("Enter the age"))
salary = int(input("Enter the salary"))

query = "Insert into sal values('{}',{},{})".format(name,age,salary)
cursor.execute(query)
con.commit()

