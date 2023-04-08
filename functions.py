from tkinter import *
from tkinter import filedialog as fd
def file(title):
    the_file = fd.askopenfilename(  
      title = title,  
      filetypes = [("Text Files", "*.*")]  
      )  