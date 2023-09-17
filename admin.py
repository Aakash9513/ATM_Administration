# This file is for the admin

import mysql.connector
import sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="atm_db"
)

mycursor = mydb.cursor()

def authenticateion_user():
    account_number = int(input("Enter the user account number: "))
    pin = int(input("Enter the PIN: "))

    sql = "SELECT * FROM users WHERE account_number = %s AND pin_admin = %s"
    mycursor.execute(sql, (account_number, pin))
    user = mycursor.fetchone()

    if user:
        return user
    else:
        print("Authentication failed. Please try again.")
        return None


def check_balance(user):
    response = input("Do you want to view Balance (YES/NO): ").upper()
    if response == "YES":
        print(f"Your account balance is ₹{user[3]:.2f}")

def main_function():
    print("ATM")
    user = None

    while not user:
        user = authenticateion_user()

    while True:
        print("1->Check_Balance")
        print("2->Exit")
        
        try:
            user_choice = int(input("Enter your choice number: "))
            if user_choice == 1:  
                check_balance(user)    
            elif user_choice == 2:
                sys.exit()
            else:
                print("Type only 1, 2, 3, or 4.")
        except ValueError:
            print("Please type a number only.")


def admin_authenticateion():
    admin_id = int(input("Enter your admin ID: "))
    pin = int(input("Enter your PIN: "))

    sql = "SELECT * FROM admin_login WHERE admin_id = %s AND pin_number = %s"
    mycursor.execute(sql, (admin_id, pin))
    user = mycursor.fetchone()

    if user:
        return user
    else:
        print("Authentication failed. Please try again.")
        return None


def admin_login():
    print("Admin login")
    user = None

    while not user:
        user = admin_authenticateion()
    
    while True:
        print("Do you want to see users account")
        print("If yes press 1")
        print("If no press 2")
        
        try:
            admin_choice = int(input("Enter your choice number: "))
            if admin_choice == 1:  
                main_function()
            elif admin_choice == 2:  
                sys.exit()
        except ValueError:
            print("Please type yes or no.")

if __name__ == "__main__":
    admin_login()
