# User defined
import p10

import random
import math
import tkinter

def onclick():
    print('hello')

window = tkinter.Tk()
b = tkinter.Button(window, text="Click Me", command=onclick)
b.pack()

window.mainloop()


##x = p10.power(2, 20)
##y = p10.add(10, 20) + p10.add(3, 9) - p10.power(2, 3)
##

##x = random.randint(1, 100)
##y = math.sin(90)
##
##
##r = 10
##a = math.pi * r ** 2

