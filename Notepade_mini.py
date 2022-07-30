from tkinter import *
import tkinter.messagebox as tmsg
import wikipedia
import webbrowser
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def new_file():
    global file
    root.title("Untitled-Notepad")
    file = None
    text_area.delete(1.0, END)


def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", '*.*'), ("Text Documents", '*.txt')])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file).split('.')[0] + '-Notepad')
        text_area.delete(1.0, END)
        f = open(file, 'r')
        text_area.insert(1.0, f.read())
        f.close()


def save_file():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled", defaultextension=".txt",
                                 filetypes=[("All Files", '*.*'), ("Text Documents", '*.txt')])
        if file == '':
            file = None
        else:
            f = open(file, 'w')
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file).split('.')[0] + '-Notepad')
    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()
        root.title(os.path.basename(file).split('.')[0] + '-Notepad')


def exit_app():
    root.destroy()


def cut_text():
    text_area.event_generate("<<Cut>>")


def copy_text():
    text_area.event_generate("<<Copy>>")


def paste_text():
    text_area.event_generate("<<Paste>>")


def about():
    print("https://en.wikipedia.org/wiki/Windows_Notepad#History")
    summary = wikipedia.summary(title="Windows_Notepad#History")
    msg_rply = tmsg.askyesno('About Notepad', f'{summary} \n Do you want to read more?')
    if msg_rply == YES:
        webbrowser.open("https://en.wikipedia.org/wiki/Windows_Notepad#History")


# defining root screen
root = Tk()
root.title("Untitled - Notepad")
root.geometry("500x650")
file = None

# creating a menubar
menubar = Menu(root)
root.config(menu=menubar)

# creating File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_app)
menubar.add_cascade(label='File', menu=file_menu)

# creating Edit menu
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='paste', command=paste_text)
menubar.add_cascade(label='Edit', menu=edit_menu)

# creating Help menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='About', command=about)
menubar.add_cascade(label='Help', menu=help_menu)

# creating Textarea
text_area = Text(root, font='Arial 12')
text_area.pack(expand=True, fill=BOTH)

# adding scrollbar
scroll1 = Scrollbar(text_area)
scroll1.pack(side=RIGHT, fill=Y)
scroll1.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll1.set)
root.mainloop()
