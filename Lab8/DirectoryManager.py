
import logging
import os.path
from os import path
from datetime import date


class Contact:

    def __init__(self, name, email, age=0, country="-"):
        self.name = name
        self.email = email
        self.age = age
        self.country = country
    
    def __str__(self):
        return ("Name: " + self.name + ", Email Address: " + self.email + ", Age: " + str(self.age) + ", Country: " + self.country).strip()

class Directory:

    def __init__(self):
        self.contactsFilePath = "contacts.txt"
        self.contacts = []
        self.loadContacts()
    
    def loadContacts(self):        
        FIELD_DELIMITER = "##" 
        if path.exists(self.contactsFilePath):
            contactsFile = open(self.contactsFilePath, "r")
            logging.info("File found and loaded")
        else:
            contactsFile = open(self.contactsFilePath, "w+")
            logging.info("New contacts file initializated")
        
        for contact in contactsFile.readlines():
            contactFields = contact.split(FIELD_DELIMITER)
            self.contacts.append(Contact(contactFields[0], contactFields[1], contactFields[2], contactFields[3]))
        contactsFile.close()        
    
    def saveContactsInFile(self):       
        FIELD_DELIMITER = "##" 
        contactsFile = open(self.contactsFilePath, "w")
        for contact in self.contacts:
            contactString = (contact.name + FIELD_DELIMITER + contact.email + FIELD_DELIMITER + str(contact.age) + FIELD_DELIMITER + contact.country).strip() + "\n"
            contactsFile.write(contactString) 
            logging.info("Save contacts in file %s", contactString)
        contactsFile.close()
    
    def addContact(self, contact):
        if self.searchContact(contact.email) == None:
            logging.info("Contact %s added successfully", contact)
            self.contacts.append(contact)
            self.saveContactsInFile()
        else:
            logging.info("Contact could not be added")
            logging.debug(msg)
            logging.info(msg)

    def deleteContact(self, contactEmail):
        contactIndex = self.searchContactIndex(contactEmail)
        if contactIndex != -1:
            logging.info("Contact %s deleted", contactEmail)
            del self.contacts[contactIndex]
            self.saveContactsInFile()
            return True
        else:
            logging.info("Contact not found %s", contactEmail)
            return False

    def searchContact(self, contactEmail):
        contactIndex = self.searchContactIndex(contactEmail)
        if contactIndex == -1:
            return None
        else:
            return self.contacts[contactIndex]

    def searchContactIndex(self, contactEmail):
        index = -1
        contactFound = False
        logging.info('Looking for contact %s', contactEmail)
        for contact in self.contacts:
            index += 1
            if contact.email == contactEmail:   
                logging.info('Contact found in index %d', index)  
                contactFound = True          
                break
        if contactFound:
            return index    
        logging.info('Contact not found')   
        return -1

    def showAllContacts(self):
        for contact in self.contacts:
            print(contact)


def initializeDirectory():
    logging.info('Directory Initialization')
    x = Directory()
    logging.info('Directory Initialization successful')
    return x


def runProgram(directory):
    exit = False
    while not(exit):

        print("What would you like to do?")
        print("1) Add contact")
        print("2) Delete contact")
        print("3) Show all contacts")
        print("4) Search contact")
        print("5) Exit")
        option = input()

        if option == "1":
            print("Enter the next information:\n")
            name = input("Contact Name: ")
            email = input("Contact Email: ")
            age = input("Contact Age: ")
            country = input("Contact Country: ")
            newContact = Contact(name, email, str(age), country)
            directory.addContact(newContact)
            print("Contact added\n")
        elif option == "2":
            email = input("Enter contact email to delete or type 'exit' to return to the main menu: ")
            if email != "exit":
                if directory.deleteContact(email):
                    print("Contact deleted.\n")
                else:
                    print("Contact not found.\n")
        elif  option == "3":
            print("Contacts in directory\n")
            directory.showAllContacts()
        elif option == "4":
            email = input("Enter contact email to delete or type 'exit' to return to the main menu: ")
            if email != "exit":
                contact = directory.searchContact(email)
                if contact is not None:
                    print(contact)
                else:
                    print("Contact not found.\n")

        elif option == "5":
            print("Bye!")
            exit = True
            today = date.today()
            logging.info(" System shut down on %s", today)
        else:
            print("Option not valid.\n")


if __name__ =="__main__":       
    today = date.today()
    logging.basicConfig(level=logging.DEBUG)
    logging.info(" System started on %s", today)
    x = initializeDirectory()
    runProgram(x)