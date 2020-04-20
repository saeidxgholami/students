import contact


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

# Display all contacts
def display_contact(filename):
    contacts = contact.read(filename)
    for i in contacts:
        print(i, end='')



def menu():
    FILENAME = 'test.txt'
    while True:
        display_menu()
        response = input('Choose from menu please\n> ')

        if response == '1':
            name = input('Name: ')
            phone = input('Phone: ')
            r = contact.create(FILENAME, name, phone)
            if r:
                print('succ')
            else:
                print('not succ')
        elif response == '2':
            display_contact(FILENAME)
        elif response == '3':
            name = input('Name to update: ')
            contacts = contact.read(FILENAME)
            found = contact.find(contacts, name)
            if found:
                print('Found')
                print('Enter new info to update')
                new_name = input('New Name: ')
                new_phone = input('New Phone: ')
                new_contact = '{}:{}\n'.format(new_name, new_phone)
                updated_contacts = contact.update(contacts, found, new_contact)
                if updated_contacts:
                    contact.write(FILENAME, updated_contacts)
                    print('succ')
                else:
                    print('not updated')
            else:
                print('not found')
        elif response == '4':
            name = input('Name to update: ')
            contacts = contact.read(FILENAME)
            result = contact.delete(contacts, name)
            if result:
                contact.write(FILENAME, result)
            else:
                print('not deleted')
            
            
        elif response == '5':
            name = input('Name to update: ')
            contacts = contact.read(FILENAME)
            found = contact.find(contacts, name)
            if found:
                print('Found', found)
            else:
                print('not found')
                
        elif response == '6':
            break


menu()
