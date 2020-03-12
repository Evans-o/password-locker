#!/usr/bin/env python3.6
from password import Password

def create_PASSWORD(fname,lname,phone,email,password):
    '''
    Function to create a new password
    '''
    new_password = Password(fname,lname,phone,email,password)
    return new_password

def save_passwords(password):
    '''
    Function to save password
    '''
    password.save_password()

def del_password(password):
    '''
    Function to delete a password
    '''
    contact.delete_password()

def find_password(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Password.find_by_number(number)

def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Password.password_exist(number)

def display_passwords():
    '''
    Function that returns all the saved contacts
    '''
    return Password.display_passwords()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cp - create a new pssword, dp - display passwords, fp -find a password, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cp':
                            print("New password")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()

                            print("password...")
                            password=input()


                            save_passwords(create_password(f_name,l_name,p_number,e_address,password)) # create and save new contact.
                            print ('\n')
                            print(f"New Password {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dp':

                            if display_passwords():
                                    print("Here is a list of all your passwords")
                                    print('\n')

                                    for password in display_passwords():
                                            print(f"{password.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fp':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_passwords(search_number):
                                    search_password = find_password(search_number)
                                    print(f"{search_password.first_name} {search_password.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_password.phone_number}")
                                    print(f"Email address.......{search_password.email}")
                                    print(f"password..{search_number_password.password}")
                            else:
                                    print("That password does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()