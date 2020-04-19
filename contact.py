import pyperclip
class Contact:
    """
    Class that generates new instances of contacts
    """
    contact_list = [] # Empty contact list
    def __init__(self,first_name,last_name,user_phone,email):

        # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.user_phone = user_phone
        self.email = email
        
        # save contact
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)

    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: User Phone to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.user_phone == number:
                return contact
    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: User Phone to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.user_phone == number:
                    return True

        return False
    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list

    # paster with pyperclip
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)   
                
pass