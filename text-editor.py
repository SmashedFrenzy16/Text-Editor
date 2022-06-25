from tkinter import *
from tkinter.filedialog import asksaveasfilename

root = Tk()
rooot.title("WordEdit")
root.geometry("600x600")

title = Label(root, text='WordEdit', font=('bold', 20), bg='light grey').pack()

scrollbar = Scrollbar(root).pack(side = RIGHT, fill = Y)

editor = Text(root, width = 400, height = 450, yscrollcommand = scrollbar.set).pack(fill = BOTH)

scrollbar.config(command = editor.yview)

buttonSave = Button(root, text = 'Save', font = ('normal', 10), command = save, bg='purple')

def save():
  
  filepath = asksaveasfilename(defaultextension = "txt", filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")])
  
  if not filepath:
    
    return
  
    with open(filepath, "w") as output_file:
      
      text = editor.get(1.0, tkinter.END)
      output_file.write(text)
   root.title(f"Title - {filepath}")
  


root.mainloop()
