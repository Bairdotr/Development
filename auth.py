
# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = input("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            print(user)
            print("in login")
            database.create_auth_session_file(account_number_from_user, user)
            bank_operation(account_number_from_user, user)
            #database.create_auth_session_file(account_number_from_user, user)
            #apparently putting this line of code never created the auth session file and never prints finish login
            print("finish login")


        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(account_number, user):
    print("Welcome %s %s " % (user[0], user[1]))
    #print(user)
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))


    if selected_option == 1:

        deposit_operation(account_number, user)
    elif selected_option == 2:

        withdrawal_operation(account_number, user)
    elif selected_option == 3:

        logout(account_number)
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(account_number, user)


def withdrawal_operation(account_number, user):
    print("Withdrawal, your current balance is " + get_current_balance(user))
    withdrawl = int(input("How much would you like to withdraw? \n"))
    if withdrawl > int(get_current_balance(user)):
        print("Must withdrwawl an amount less than " + get_current_balance(user) + "\n")
        withdrawal_operation(account_number, user)
    else:
        set_current_balance(user, str(int(get_current_balance(user))-withdrawl))
        database.update(account_number, user)
        print("Your current balance is " + get_current_balance(user))
    bank_operation(account_number, user)
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_operation(account_number, user):
    print("Deposit Operations: You're current balance is " + get_current_balance(user))
    deposit = int(input("How much would you like to deposit?\n"))
    balance = int(get_current_balance(user))
    balance += deposit
    set_current_balance(user, str(balance))
    print("Current balance is " + get_current_balance(user) + "\n")
    print("***")
    database.update(account_number,user)
    bank_operation(account_number, user)

    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout(account_number):
    database.delete_auth_session(account_number)
    login()


init()
