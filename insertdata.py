import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd= 'Ankit@8285',
                database='student')

cursor = con.cursor()

#update
name = input("Enter the name")
age = int(input("Enter the age"))

query = "Update detail set age={} where name ='{}'".format(age,name)
cursor.execute(query)
con.commit()
print("Data value updated!!")




