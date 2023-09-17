# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345",
#     database="atm_db"
# )

# mycursor=mydb.cursor()

def transaction():

    print("1-> Do you want to procied")
    print("2-> Cancel")

    user=int(input("entter your choice"))
    if user==1:
        import user
        user.main_function()
    else:
        print("thank you for your time")

def main():
    print("Welcome SMA Automated teller machine")
    print("1->user")
    print("2->admin")

    user=int(input("enter your number:"))
    if user==1:
        transaction()
    elif user==2:
        import admin
        admin.main_function()
    else:
        print("pls type 1 or 2 ")
main()

# *********This function is just to add data in the data base***********


# def insert_data():
#     sql="insert into users (id,user_name,account_number,balance,pin,pin_admin) values (%s,%s,%s,%s,%s,%s)"
#     id=input("enter your id")
#     user_name=input("enter your user_name")
#     account_number=input("enter your account_number")
#     pin=input("enter your pin")
#     balance=input("enter your appoinment balance")
#     pin_admin=input("enter your admin pin")  # admin will keep the pin same for all the accounts
#     values=(id,user_name,account_number,balance,pin,pin_admin)
#     mycursor=mydb.cursor(sql,values)
#     mycursor.execute(sql,values)
#     mydb.commit()
#     print("Hi your account has been added  sucesfully")

# insert_data()