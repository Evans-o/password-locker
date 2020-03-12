class Password:
    """
    Class that generates new instances of passwords.
    """

    password_list = [] # Empty password list
 # Init method up here
    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)
    def __init__(self,first_name,last_name,number,email,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password= password

    def delete_password(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Password.password_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for password in cls.password_list:
            if password.phone_number == number:
                return password

    @classmethod
    def password_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for password in cls.password_list:
            if password.phone_number == number:
                    return True

        return False

    @classmethod
    def display_passwords(cls):
        '''
        method that returns the contact list
        '''
        return cls.password_list