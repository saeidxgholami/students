# Contact Logic

# Read and return all contacts as a list
def get_contacts(filename):
    contact_file = open(filename, 'r')
    all_contacts = contact_file.readlines()
    contact_file.close()
    return all_contacts


# Write contact list to file
def write(contacts):
    f = open('contacts.txt', 'w')
    f.truncate()
    for contact in  contacts:
        f.write(contact)
    f.close()

# Create a contact
def create(name, phone):
    # operation on contact file
    contact_file = open('contacts.txt', 'a')
    contact_file.write(name + ':' + phone + '\n')
    contact_file.close()
    return True



# contacs: ['name:1234', ]
def find(contacts, name):
    for line in contacts:
        contact_name, phone = line.split(':')
        if contact_name == name:
            return line
    return False
