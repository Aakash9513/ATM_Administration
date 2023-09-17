# This File is for the user
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
    account_number = int(input("Enter your account number: "))
    pin = int(input("Enter your PIN: "))

    sql = "SELECT * FROM users WHERE account_number = %s AND pin = %s"
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


def withdraw(user):
    amount = int(input("Enter the withdrawal amount: "))
    if amount > user[3]:
        print("Insufficient funds.")
    else:
        new_balance = user[3] - amount
        update_query = "UPDATE users SET balance = %s WHERE id = %s"
        mycursor.execute(update_query, (new_balance, user[0]))
        mydb.commit()
        print(f"Withdrawal successful. Your new balance is ₹{new_balance:.2f}")
      

def insert_money(user):
    amount = float(input("Do you want to insert money: "))
    new_balance = user[3] + amount
    sql = "UPDATE users SET balance = %s WHERE id = %s"
    mycursor.execute(sql, (new_balance, user[0]))
    mydb.commit()
    print(f"Amount added successfully.\nYour new balance is ₹{new_balance:.2f}")


def main_function():
    print("ATM")
    user = None

    while not user:
        user = authenticateion_user()

    while True:
        print("1->Check_Balance")
        print("2->Withdraw")
        print("3->Insert_money")
        print("4->Exit")
        print("To Create Account Pls Contact The Nearest Bank")

        try:
            user_choice = int(input("Enter your choice number: "))
            if user_choice == 1:  
                check_balance(user)    
            elif user_choice == 2:
                withdraw(user)
            elif user_choice == 3:
                insert_money(user)
            elif user_choice == 4:
                sys.exit()
            else:
                print("Type only 1, 2, 3, or 4.")
        except ValueError:
            print("Please type a number only.")

if __name__ == "__main__":
    main_function()