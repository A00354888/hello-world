
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
        print("here")
        FIELD_DELIMITER = "##" 
        contactsFile = open(self.contactsFilePath, "r")
        for contact in contactsFile.readlines():
            contactFields = contact.split(FIELD_DELIMITER)
            self.contacts.append(Contact(contactFields[0], contactFields[1], contactFields[2], contactFields[3]))
        contactsFile.close()
    
    def saveContactsInFile(self):       
        FIELD_DELIMITER = "##" 
        contactsFile = open(self.contactsFilePath, "w")
        for contact in self.contacts:
            contactString = (contact.name+FIELD_DELIMITER+contact.email+FIELD_DELIMITER+str(contact.age)+FIELD_DELIMITER+contact.country).strip()+"\n"
            contactsFile.write(contactString) 
        contactsFile.close()
    
    def addContact(self, contact):
        if self.searchContact(contact.email) is None:
            self.contacts.append(contact)
            self.saveContactsInFile()

    def deleteContact(self, contactEmail):
        contactIndex = self.searchContactIndex(contactEmail)
        if contactIndex != -1:
            print("Deleted index "+str(contactIndex))
            del self.contacts[contactIndex]
            self.saveContactsInFile()

    def searchContact(self, contactEmail):
        contactIndex = self.searchContactIndex(contactEmail)
        print (contactIndex)
        if contactIndex == -1:
            return None
        return self.contacts[contactIndex]

    def searchContactIndex(self, contactEmail):
        index = -1
        contactFound = False
        for contact in self.contacts:
            index += 1
            if contact.email == contactEmail:      
                contactFound = True          
                break
        if contactFound:
            return index    
        return -1

    def showAllContacts(self):
        for contact in self.contacts:
            print(contact)


x = Directory()
contact = Contact("Eduardo Siordia", "eduardo.montes@test.com", 31, "MX")
contact2 = Contact("Karlos Robles", "karlos@gmail.com")
contact3 = Contact("Isela Torres", "isela2@test.com")
print("----------ORIGINAL-------------")
x.showAllContacts()
print("-----------------------")
x.addContact(contact)
x.addContact(contact2)
x.addContact(contact3)
x.showAllContacts()

print(x.searchContact("eduardo.montes@test.com"))
x.deleteContact("karlos@gmail.com")