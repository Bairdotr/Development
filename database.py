
# create record
# update record
# read record
# delete record
# CRUD

# find user

import os
import validation

user_db_path = "data/user_record/"
user_session_path = "data/auth_session/"


def create(user_account_number, first_name, last_name, email, password):

    # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then deleted created file

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(user_account_number):

        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(user_account_number) + ".txt", "x")
        print("Get to 1")

    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not does_file_contain_data:
            delete(user_account_number)
            print("Get to 2")

    else:

        f.write(str(user_data));
        completion_state = True
        print("Get to 3")

    finally:

        f.close();
        return completion_state
        print("Get to 4")


def read(user_account_number):

    # find user with account number
    # fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def update(user_account_number, user):
    print("Updating account")
    updated_info = ""
    i = 0
    for elem in user:
        if i < len(user)-1:
            updated_info += elem + ","
            i+=1
        else:
            updated_info += elem
    print(updated_info)
    f = open(user_db_path + str(user_account_number) + ".txt", "w")

    f.write(updated_info)
    f.close()

def create_auth_session_file(account_number, user):

    f = open(user_session_path + str(account_number) + ".txt", "w")
    file_info = ""
    i = 0
    for elem in user:
        if i < len(user)-1:
            file_info += elem + ","
            i+=1
        else:
            file_info += elem
    print(file_info)
    f.write(file_info)
    f.close()


def delete_auth_session(account_number):

    is_delete_successful = False

    if os.path.exists(user_session_path + str(account_number) + ".txt"):
        try:

            os.remove(user_session_path + str(account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful

    # print("update user record")
    # print(read(user_account_number))
    # user = str.split(read(user_account_number), ',')
    #
    # balance = str(int(user[4]) + int(number))
    # print(balance)
    # user[4] = balance
    # print(user)
    # updated_info = ""
    # i = 0
    # for elem in user:
    #     if i < len(user)-1:
    #         updated_info += elem + ","
    #         i+=1
    #     else:
    #         updated_info += elem
    # print(updated_info)
    # print("end")
    # f = open(str(user_account_number)+".txt", "w")
    # f.write(updated_info)
    # f.close()
    # f = open(str(user_account_number)+".txt", "r")
    # print(f.read)



    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(user_account_number):

    # find user with account number
    # delete the user record (file)
    # return true

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful


def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number) + ".txt":

            return True

    return False


def authenticated_user(account_number, password):

    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False


# print(read(5878925801))
# print(update(5878925801, 100))
# print("testing write")
# print(read(5878925801))
