import tkinter
from tkinter import *
import cryptocode

def btn_encrypt_click():
    print("Make an encryption")
    encrypted_string = cryptocode.encrypt(text_area.get(1.0,tkinter.END),entry_password.get())
    text_area.delete(1.0,tkinter.END)
    text_area.insert(1.0, encrypted_string)

def btn_decrypt_click():
    print("Make a decryption")
    decrypted_string = cryptocode.decrypt(text_area.get(1.0,tkinter.END),entry_password.get())
    text_area.delete(1.0,tkinter.END)
    text_area.insert(1.0, decrypted_string)

#window setting for tkinter--> Set the size and location of the cpu.
window = tkinter.Tk()
window.title("Encryption and decryption")
window.geometry("380x400+800+300")
window.resizable(False, False)

#label
lb_text = Label(window,width = 10, text = "password:")
lb_text.grid(row=0, column = 0)

#input password
entry_password = Entry(window, width = 20, show = '*')
entry_password.grid(row=0, column = 1)

#encryption button
btn_ok = tkinter.Button(window, overrelief = "solid", text = "encrytion", width = 10,
                        command = btn_encrypt_click, repeatdelay = 1000, repeatinterval = 100)
btn_ok.grid(row = 0, column=3, padx = 5)

#decryption button
btn_ok = tkinter.Button(window, overrelief = "solid", text = "decrytion", width = 10,
                        command = btn_encrypt_click, repeatdelay = 1000, repeatinterval = 100)
btn_ok.grid(row = 0, column=2, padx = 5)

#text area
text_area = Text(window)
window.grid_rowconfigure(0,weight =1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky = N+E+S+W, row=2, columnspan=4, padx=10, pady=10)

#Run the main loop to prevent cpu from shutting down.
window.mainloop()
