import unittest
from password import Password
import pyperclip

class Testpasswordnew_password(unittest.TestCase):

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password('Evans','Opindi','0740772578','evansopindi@yahoo.com','evracheche1999') # create passwordnew_password object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
    

        self.assertEqual(self.new_password.first_name,"Evans")
        self.assertEqual(self.new_password.last_name,"Opindi")
        self.assertEqual(self.new_password.phone_number,"0740772578")
        self.assertEqual(self.new_password.email,"evansopindi@yahoo.com")
        self.assertEqual(self.new_password.password,"evracheche1999")
        
    def create_Password(fname,lname,phone,email,password):
        '''
        Function to create a new contact
        '''
        new_password = Password(fname,lname,phone,email,password)
        return new_password


    def test_save_password(self):
        '''
        test_save_password test case to test if the password object is saved into
         the password list
        '''
        self.new_password.save_password() # saving the new password
        self.assertEqual(len(Password.password_list),1)


    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Password.password_list = []

# other test cases here
    def test_save_multiple_password(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","0712345678","test@user.com","evracheche") # new contact
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)


    # More tests above
    def test_delete_password(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","0712345678","test@user.com","evracheche") # new contact
            test_password.save_password()

            self.new_password.delete_password()# Deleting a contact object
            self.assertEqual(len(Password.password_list),1)

    def test_find_password_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_password.save_password()
        test_password = Password("Test","user","0711223344","test@user.com","evracheche") # new contact
        test_password.save_password()

        found_password = Password.find_by_number("0711223344")

        self.assertEqual(found_password.email,test_password.email)

    def test_password_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_password.save_password()
        test_password = Password("Test","user","0711223344","test@user.com","password") # new contact
        test_password.save_password()

        password_exists = Password.password_exist("0711223344")

        self.assertTrue(password_exists)

    def test_display_all_passwords(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Password.display_passwords(),Password.password_list)


if __name__ == '__main__':
    unittest.main()