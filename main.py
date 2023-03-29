from customtkinter import *
import customtkinter
flag = ''
customtkinter.set_appearance_mode("Dark")
def Landing():
    global flag
    app = CTk()
    def landingnext():
        nonlocal app
        flag = 'Landing Next Triggered'
        app.destroy()
    l = CTkButton(app, text = "Next", command = landingnext).pack()
    app.mainloop()
Landing()
if flag == 'Landing Next Triggered':
    Two()