##Author: Jeffrey Chang
##https://github.com/JustaLackey
##Date 8/7/2013

from tkinter import *
from tkinter import ttk
from Crypter import *

def enc(*args):
    try:
        value = message.get()
        keyg = key.get()
        cipher.set(Crypter.encrypt2(value,keyg))
    except ValueError:
        pass

def dec(*args):
    try:
        value = cipher.get()
        keyg = key.get()
        message.set(Crypter.encrypt2(value,keyg))
    except ValueError:
        pass
    
    
root = Tk()
root.title("Crypt")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

message = StringVar()
cipher = StringVar()
key = StringVar()

key_entry = ttk.Entry(mainframe, width=80, textvariable=key)
key_entry.grid(column=2, row=1, sticky=(W, E))

msg_entry = ttk.Entry(mainframe, width=80, textvariable=message)
msg_entry.grid(column=2, row=2, sticky=(W, E))

cipher_entry = ttk.Entry(mainframe, width=80, textvariable=cipher)
cipher_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Encrypt", command=enc).grid(column=4, row=2, sticky=W)
ttk.Button(mainframe, text="Decrypt", command=dec).grid(column=4, row=3, sticky=W)

ttk.Label(mainframe, text="Key").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Msg").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Cipher").grid(column=1, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

key_entry.focus()

root.bind('<Return>', enc)
root.bind('<Return>', dec)

root.mainloop()
