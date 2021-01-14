"""https://python-textbok.readthedocs.io/en/latest/
Introduction_to_GUI_Programming.html#putting-it-all-together"""
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title = "yog_soggoth"

mainframe = ttk.Frame(root, padding ="3 3 12 12")
mainframe.grid(column=0, row = 0, sticky = (N,W,E,S))
innerframe = ttk.Frame(mainframe, padding = "3 3 12 12")
innerframe.grid(column = 0, row = 0, sticky = (N,W,E,S))

root.columnconfigure(0,weight = 1)
root.rowconfigure(0,weight = 1)

root.mainloop()
