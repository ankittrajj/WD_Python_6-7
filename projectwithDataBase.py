import mysql.connector as c
con = c.connect(host="localhost",
                user='root',
                passwd="Ankit@8285",
                database='bank')

cursor = con.cursor()

print("Bank management System")




while True:
    choice = input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Account Details\n5.Exit")
# open account
    if choice == '1':
        name = input("Enter you name")
        mobile = int(input("Enter your mobile number"))
        age = int(input("Enter your age"))
        amount = int(input("Enter the amount to open the account"))
        query = "Insert into detail values('{}',{},{},{})".format(name,mobile,age,amount)
        cursor.execute(query)
        con.commit()
        print("Account open successfully!!")


    # cash deposit

    elif choice == '2':
        amount = int(input("Enter the amount to deposit"))
        name=input("Enter the name")

        query = "Update detail set amount={} where name='{}'".format(amount,name)
        cursor.execute(query)
        con.commit()
        print("Updated successfully!!")

    # cash withdrawal
    elif choice == '3':

        amount=int(input("Enter the amount to withdrawl"))
        name=input("enter the name")

        query="update detail set amount={} where name='{}'".format(amount,name)
        cursor.execute(query)
        con.commit()
        print(" updated!!")


    #
    # Account details
    elif choice == '4':
        query = "select * from detail"
        cursor.execute(query)

        account_details = cursor.fetchall()
        print(account_details)
        con.commit()


    if choice=='5':
        break;




# make a add on feature for cash deposit.
# make a one more option for account update.


