import pymysql

try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='bankingapp')
    print("Database connected!")
except Exception as e:
    print(e)
    
cr=dbcon.cursor()
# Create a Table
create_tbl="create table if not exists banker(id integer primary key auto_increment,username text unique,password text)"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)   
    
create_tbl="create table if not exists customers(id integer primary key auto_increment,username text unique,password text,balance decimal(10,2))"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)   


dbcon.commit()
dbcon.close()

import database

# Initialize the database
database.create_database()

# Function to register a banker
def banker_register():
    conn = database.connect()
    cursor = conn.cursor()
    
    username = input("Enter banker username: ")
    password = input("Enter banker password: ")
    
    cursor.execute("INSERT INTO bankers (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    print("Banker registered successfully!")

# Function to login as a banker
def banker_login():
    conn = database.connect()
    cursor = conn.cursor()
    
    username = input("Enter banker username: ")
    password = input("Enter banker password: ")
    
    cursor.execute("SELECT * FROM bankers WHERE username = ? AND password = ?", (username, password))
    banker = cursor.fetchone()
    
    if banker:
        print("Banker login successful!")
    else:
        print("Banker login failed. Invalid credentials.")
    
    conn.close()

# Function to view all customers
def view_customers():
    conn = database.connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    
    for customer in customers:
        print(f"ID: {customer[0]}, Username: {customer[1]}, Balance: ${customer[3]:.2f}")
    
    conn.close()

# Function to register a customer
def customer_register():
    conn = database.connect()
    cursor = conn.cursor()
    
    username = input("Enter customer username: ")
    password = input("Enter customer password: ")
    
    cursor.execute("INSERT INTO customers (username, password, balance) VALUES (?, ?, 0)", (username, password))
    conn.commit()
    conn.close()
    print("Customer registered successfully!")

# Function to login as a customer
def customer_login():
    conn = database.connect()
    cursor = conn.cursor()
    
    username = input("Enter customer username: ")
    password = input("Enter customer password: ")
    
    cursor.execute("SELECT * FROM customers WHERE username = ? AND password = ?", (username, password))
    customer = cursor.fetchone()
    
    if customer:
        print("Customer login successful!")
        customer_menu(customer)
    else:
        print("Customer login failed. Invalid credentials.")
    
    conn.close()

# Function to display the customer menu
def customer_menu(customer):
    while True:
        print("\nCustomer Menu:")
        print("1. Withdraw Amount")
        print("2. Deposit Amount")
        print("3. View Balance")
        print("4. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            withdraw_amount(customer)
        elif choice == '2':
            deposit_amount(customer)
        elif choice == '3':
            view_balance(customer)
        elif choice == '4':
            print("Customer logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to withdraw money for a customer
def withdraw_amount(customer):
    conn = database.connect()
    cursor = conn.cursor()
    
    amount = float(input("Enter the amount to withdraw: "))
    
    if amount <= 0:
        print("Invalid amount. Please enter a positive amount.")
    elif customer[3] < amount:
        print("Insufficient balance.")
    else:
        cursor.execute("UPDATE customers SET balance = balance - ? WHERE id = ?", (amount, customer[0]))
        conn.commit()
        print(f"Withdrew ${amount:.2f}. New balance: ${customer[3] - amount:.2f}")
    
    conn.close()

# Function to deposit money for a customer
def deposit_amount(customer):
    conn = database.connect()
    cursor = conn.cursor()
    
    amount = float(input("Enter the amount to deposit: "))
    
    if amount <= 0:
        print("Invalid amount. Please enter a positive amount.")
    else:
        cursor.execute("UPDATE customers SET balance = balance + ? WHERE id = ?", (amount, customer[0]))
        conn.commit()
        print(f"Deposited ${amount:.2f}. New balance: ${customer[3] + amount:.2f}")
    
    conn.close()

# Function to view balance for a customer
def view_balance(customer):
    print(f"Your balance: ${customer[3]:.2f}")

# Main program loop
while True:
    print("\nBanking Application Menu:")
    print("1. Banker")
    print("2. Customer")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("\nBanker Menu:")
        print("1. Register")
        print("2. Login")
        print("3. View All Customers")
        banker_choice = input("Enter your choice: ")
        if banker_choice == '1':
            banker_register()
        elif banker_choice == '2':
            banker_login()
        elif banker_choice == '3':
            view_customers()
        else:
            print("Invalid choice. Please try again.")
    elif choice == '2':
        print("\nCustomer Menu:")
        print("1. Register")
        print("2. Login")
        customer_choice = input("Enter your choice: ")
        if customer_choice == '1':
            customer_register()
        elif customer_choice == '2':
            customer_login()
        else:
            print("Invalid choice. Please try again.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
