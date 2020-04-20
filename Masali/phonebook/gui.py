# Graphical User Interface
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import contact


def create_contact(namebox, phonebox):
	name = namebox.get()
	phone = phonebox.get()
	contact.create(name, phone)
	# messagebox.showinfo('Contact Creation', 'Contact created successfuly.')
	# clear content of namebox and phonebox
	namebox.delete(0, 'end')
	phonebox.delete(0, 'end')


def display_contacts(root):
	form = tk.Toplevel(root)
	form.title('All Contacts')
	form.geometry('300x200')
	contact_list = contact.get_contacts('contacts.txt')
	contacts = ''.join(contact_list)
	contacts_label = ttk.Label(form, text=contacts)
	contacts_label.pack()

def search(namebox):
	name = namebox.get()
	contacts = contact.get_contacts('contacts.txt')
	found = contact.find(contacts, name)
	if found:
		messagebox.showinfo('Contact Inforamtion', found)
	else:
		messagebox.showinfo('Contact Inforamtion', 'Contact not found!')
	


def find_contact(root):
	form = tk.Toplevel(root)
	form.title('Find a Contact')
	ttk.Label(form, text='Enter a name to search.').pack()
	namebox = ttk.Entry(form)
	namebox.pack(pady=10)
	search_button = ttk.Button(form, text='Search')
	search_button.pack(pady=10)
	search_button.config(command=lambda: search(namebox))




root = tk.Tk()
root.title('Phonebook App')

ttk.Label(root, text="Name").grid(row=0, column=0, pady=10, padx=10)
ttk.Label(root, text="Phone").grid(row=1, column=0, pady=10, padx=10)

# Widget defination
name_box = ttk.Entry(root)
phone_box = ttk.Entry(root)
create_button = ttk.Button(root, text='Create Contact')
display_button = ttk.Button(root, text='Display Contacts')
find_button = ttk.Button(root, text='Find a Contact')

# Grid the widgets to display
name_box.grid(row=0, column=1, padx=10)
phone_box.grid(row=1, column=1)
create_button.grid(row=2, column=1, sticky='ew', padx=10, pady=(10, 0))
display_button.grid(row=3, column=1, sticky='ew', padx=10, pady=5)
find_button.grid(row=4, column=1, sticky='ew', padx=10, pady=5)

# Widget configs
create_button.config(command=lambda: create_contact(name_box, phone_box))
display_button.config(command=lambda: display_contacts(root))
find_button.config(command=lambda: find_contact(root))


root.mainloop()