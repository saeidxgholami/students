# A contact contain a name and a phone
# CRUD: Create, Read, Update, Delete



names = []
phones = []


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
        contact_file = open('contacts.txt', 'r')
        all_contacts = contact_file.readlines()
        temp_contacts = all_contacts.copy()
        for line in all_contacts:
            name, phone = line.split(':')
            # if contact contain who
            if name == who:
                # update
                print('found')
                new_name = input("New Name: ")
                new_phone = input("New Phone: ")
                index_who = temp_contacts.index(line)
                temp_contacts[index_who] = new_name + ':' + new_phone + '\n'
                # write new data
                # delete all data in file
                f = open('contacts.txt', 'w')
                f.truncate()
                # write contact with new name and new phone to file
                for contact in  temp_contacts:
                    f.write(contact)
                f.close()
                break
                
    # Delete a contact
    elif user_response == '4':
        pass
    # find
    elif user_response == '5':
        who = input('Enter contact name to update: ')
        contact_file = open('contacts.txt', 'r')
        all_contacts = contact_file.readlines()
        x = 0
        for line in all_contacts:
            name, phone = line.split(':')
            if name == who:
                print('Contact Found:')
                print('Name: ', name)
                print('Phone: ', phone)
                x = 1
                break

        if x == 0:
            print('Not Found')
                
            
    # exit from app  
    elif user_response == '6':
        break
    
        
    # None of the above, wrong choose
    else:
        print('Invalid choose')

print('End of program')
