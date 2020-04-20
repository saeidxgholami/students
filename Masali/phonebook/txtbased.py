# TUI: Terminal User Interface

import os
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
def display_contact():
    contact_list = contact.get_contacts('contacts.txt')
    for line in contact_list:
        print(line, end='')

def get_info():
    name = input("Name: ")
    phone = input("Phone: ")
    return name, phone

while True:
    os.system('clear')
    display_menu()
    # get user choose
    user_response = input('Choose from menu please\n> ')

    # Create contact
    if user_response == '1':
        name, phone = get_info()
        if contact.create(name, phone):
            print("Success.")
        input('Enter any key to back to menu ...')
    # Display contacts
    elif user_response == '2':
        display_contact()
        input('Enter any key to back to menu ...')
    # Update a contact
    elif user_response == '3':
        who = input('Enter contact name to update: ')
        contacts = contact.get_contacts('contacts.txt')
        row_contact = contact.find(contacts, who)
        if row_contact:
            new_name, new_phone = get_info()
            index_who = contacts.index(row_contact)
            contacts[index_who] = new_name + ':' + new_phone + '\n'
            # write all contacts along side new contact
            contact.write(contacts)
        else:
            print('Contact not found!')
        input('Enter any key to back to menu ...')       
    # Delete a contact
    elif user_response == '4':
        who = input('Enter contact name to delete: ')
        contacts = contact.get_contacts('contacts.txt')
        row_contact = contact.find(contacts, who)
        if row_contact:
            contacts.remove(row_contact)
            contact.write(contacts)
        else:
            print('Contact Not Found!')
        input('Enter any key to back to menu ...')
    # Find Contact
    elif user_response == '5':
        who = input('Enter contact name to update: ')
        all_contacts = contact.get_contacts('contacts.txt')
        row_contact  = contact.find(all_contacts, who)
        if row_contact:
            name, phone = row_contact.split(':')
            print('Name: ', name)
            print('Phone:', phone)
        else:
            print('Not Found')
        input('Enter any key to back to menu ...')
    # exit from app  
    elif user_response == '6':
        break
   
    # None of the above, wrong choose
    else:
        print('Invalid choose')

print('End of program')