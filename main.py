from customtkinter import *
import customtkinter
flag = ''
customtkinter.set_appearance_mode("Dark")
def Landing():
    global flag
    win1 = CTk()
    def landingnext():
        nonlocal win1
        flag = 'Landing Next Triggered'
        win1.destroy()
    l = CTkButton(win1, text = "Next", command = landingnext).pack()
    app.mainloop()
Landing()