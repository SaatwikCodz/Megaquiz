def file(title):
    the_file = fd.askopenfilename(  
      title = title,  
      filetypes = [("Text Files", "*.*")]  
      )  