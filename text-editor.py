from tkinter import *
from tkinter.filedialog import asksaveasfilename

root = Tk()
rooot.title("WordEdit")
root.geometry("600x600")

title = Label(root, text='WordEdit', font=('bold', 20), bg='light grey').pack()

scrollbar = Scrollbar(root).pack(side = RIGHT, fill = Y)






root.mainloop()
