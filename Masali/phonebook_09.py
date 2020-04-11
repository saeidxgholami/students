# A contact contain a name and a phone
# CRUD: Create, Read, Update, Delete


# display menu items
def display_menu():
    menu_items = [
    '1. Add a new contact',
    '2. Display contacts',
    '3. Update a contact',
    '4. Delete a contact',
    '5. Find Contact',
    '6. Quit']
    print('*' * 20)
    for item in menu_items:
        print(item)
    print('*' * 20)


# Read and return all contacts as a list
def get_contacts():
    contact_file = open('contacts.txt', 'r')
    all_contacts = contact_file.readlines()
    contact_file.close()
    return all_contacts


# Write contact list to file
def write_contacts(contacts):
    f = open('contacts.txt', 'w')
    f.truncate()
    for contact in  contacts:
        f.write(contact)
    f.close()


# Create a contact
def create_contact(name, phone):
    # operation on contact file
    contact_file = open('contacts.txt', 'a')
    contact_file.write(name + ':' + phone + '\n')
    contact_file.close()
    print('Contact added successfuly')


# Display all contacts
def display_contact():
    contact_file = open('contacts.txt', 'r')
    all_contacts = contact_file.read()
    print(all_contacts)


# contacs: ['name:1234', ]
def find(contacts, name):
    for line in contacts:
        contact_name, phone = line.split(':')
        if contact_name == name:
            return line
    return False

    
while True:
    display_menu()
    # get user choose
    user_response = input('Choose from menu please\n> ')

    if user_response == '1':
        name = input('Name: ')
        phone = input('Phone Number: ')
        create_contact(name, phone)

    elif user_response == '2':
        display_contact()
        
    # Update a contact
    elif user_response == '3':
        who = input('Enter contact name to update: ')
        contacts = get_contacts()
        row_contact = find(contacts, who)
        if row_contact:
            new_name = input("New Name: ")
            new_phone = input("New Phone: ")
            index_who = contacts.index(row_contact)
            contacts[index_who] = new_name + ':' + new_phone + '\n'
            # write all contacts along side new contact
            write_contacts(contacts)
        else:
            print('Contact not found!')
               
    # Delete a contact
    elif user_response == '4':
        who = input('Enter contact name to delete: ')
        contacts = get_contacts()
        row_contact = find(contacts, who)
        if row_contact:
            contacts.remove(row_contact)
            write_contacts(contacts)
        else:
            print('Contact Not Found!')
        
    # find
    elif user_response == '5':
        who = input('Enter contact name to update: ')
        all_contacts = get_contacts()
        row_contact  = find(all_contacts, who)
        if row_contact:
            name, phone = row_contact.split(':')
            print('Name: ', name)
            print('Phone:', phone)
        else:
            print('Not Found')
        
    # exit from app  
    elif user_response == '6':
        break
    
        
    # None of the above, wrong choose
    else:
        print('Invalid choose')

print('End of program')
