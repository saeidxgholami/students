import tkinter as tk
import contact

from tkinter import messagebox


FILENAME = 'test.txt'

def create_contact(name_box, phone_box):
    created = contact.create(FILENAME, name_box.get(), phone_box.get())
    if created:
        messagebox.showinfo('Contact Create', 'Contact created successfuly')
        
def create_ui(root):
    name_box = tk.Entry(root)
    phone_box = tk.Entry(root)
    name_box.grid(row=0, column=0)
    phone_box.grid(row=1, column=0)
    create_button = tk.Button(root, text='Create', command=lambda: create_contact(name_box, phone_box))
    create_button.grid(row=2, column=0)


root = tk.Tk()
root.title('Phonebook App')
create_ui(root)






root.mainloop()
