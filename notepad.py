from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text_area.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Textdocuments", ".txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        text_area.delete(1.0, END)   # for overwriting the content of present file
        f = open(file, "r")
        text_area.insert(1.0, f.read())  # for reading the contents of the file till the end
        f.close()


def savefile():
    global file
    if file == None:  # if it is equal to blank string then file will not be save
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text", ".txt")])
        if file == None:
            file = None
        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            print("file save")
    else:   # we use this else becoz when we open an existing and make changes in it
        # and then try to save and try to open it again
        # if there is no else then the changes will not
        #  be saved in the file
        # save the file
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()


def exitfile():
    root.destroy()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo(" About Notepad", "Version 1.0 by Akash")


if __name__ == "__main__":
    #  creating a text area using text command
    root = Tk()
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("logo.ico")
    root.geometry("600x600")
    text_area = Text(root, font="lucida 15")
    file = None
    text_area.pack(expand=True, fill=BOTH)
    #  file menu start
    MenuBar = Menu(root)
    fileMenu = Menu(MenuBar, tearoff=0)

    # To open a new file
    fileMenu.add_command(label="New", command=newfile)

    # to open an existing file
    fileMenu.add_command(label="Open", command=openfile)
    # to save a file
    fileMenu.add_command(label="Save", command=savefile)
    fileMenu.add_separator()

    # to exit notepad
    fileMenu.add_command(label="Exit", command=exitfile)

    MenuBar.add_cascade(label="File", menu=fileMenu)
    root.config(menu=MenuBar)
    # file menu ends
    #  edit menu starts

    editMenu = Menu(MenuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=editMenu)
    root.config(menu=MenuBar)
    #  edit menu ends
    helpMenu = Menu(MenuBar, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    MenuBar.add_cascade(label="Help", menu=helpMenu)
    root.config(menu=MenuBar)

    scroll = Scrollbar(text_area)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll.set)
    root.mainloop()
