# A contact contain a name and a phone
# CRUD: Create, Read, Update, Delete

menu_items = [
    '1. Add a new contact',
    '2. Display contacts',
    '3. Update a contact',
    '4. Delete a contact',
    '5. Quit'
]

names = []
phones = []

while True:
    print('*' * 20)
    # display menu items
    for item in menu_items:
        print(item)
    print('*' * 20)
    # get user choose
    user_response = input('Choose from menu please\n> ')
    
    
    # Create a contact
    if user_response == '1':
        name = input('Name: ')
        phone = input('Phone Number: ')
        #names.append(name)
        #phones.append(phone)
        # Write name and phone to the file
        contact_file = open('contacts.txt', 'a')
        contact_file.write(name + ':' + phone + '\n')
        contact_file.close()
        print('Contact added successfuly')

    # Display all contacts
    elif user_response == '2':
        #for name, phone in zip(names, phones):
            #print(name, phone)
        contact_file = open('contacts.txt', 'r')
        all_contacts = contact_file.read()
        print(all_contacts.__repr__())
        print(all_contacts)
        
    # Update a contact
    elif user_response == '3':
        pass
    # Delete a contact
    elif user_response == '4':
        pass
    # exit from app
    elif user_response == '5':
        break
    # None of the above, wrong choose
    else:
        print('Invalid choose')

print('End of program')
