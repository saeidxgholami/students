
def write(filename, contacts):
    f = open(filename, 'w')
    for item in contacts:
        f.write(item)
        

# Append a contact in the filename
def append(filename, contact):
    f = open(filename, 'a')
    f.write(contact)
    f.close()

# Create a contact in form of 'name:phone'
def create(filename, name, phone):
    contact = '{}:{}\n'.format(name, phone)
    append(filename, contact)
    return True


# Get a contact list and a name:
# return contact if contact found
# otherwise return False
def find(contacts, name):
    for line in contacts:
        contact_name, phone = line.split(':')
        if contact_name == name:
            return line
    return False


# Get a contact list and a new and new contact info
# change contact with new info
# otherwise return Flase
def update(contacts, old_contact, new_info):
    index = contacts.index(old_contact)
    contacts[index] = new_info
    return contacts
    

# Get a contact list find name and delete it
def delete(contacts, name):
    found = find(contacts, name)
    if found:
        contacts.remove(found)
        return contacts
    return False


def read(filename):
    f = open(filename, 'r')
    contacts = f.readlines()
    f.close()
    return contacts
