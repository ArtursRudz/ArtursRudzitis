#mis ir uztaisīt programmu, kurā zemūdene spridzina burbuli
#tiek skaitīti punkti
from tkinter import *
from math import *
from random import *
logs = Tk()
garums = 700
platums = 700
logs.title("Burbuļu spridzinātājs")
a = Canvas(logs,width=garums,height=garums, bg='aqua')
a.pack()
kuga_id = a.create_oval(0,0,100,100,outline='black',width=5)



mainloop()
