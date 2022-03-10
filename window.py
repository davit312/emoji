from tkinter import *
from tkinter import ttk

import json

from vars import *
import callbacks as cb

class root():

    def __init__(self):
        self.root = Tk()

        self.root.title(txt['title'])

        self.content = ttk.Frame(self.root)
        self.content.grid(column=0, row=0)

        self.frame = ttk.Frame(self.content, borderwidth=5,)
        self.frame.grid(column=0, row=0, columnspan=8, rowspan=4)

        cb.setWindow(self)
   
    def build(self):
        self.buuildTopBar()
        self.buildCategores()

    def buuildTopBar(self):
        self.search = StringVar()
        self.search.trace_add('write', cb.onsearch)

        self.searchbar =  ttk.Entry(self.frame, textvariable=self.search, font=("",16))
        self.searchbar.grid(row=0, column=0,columnspan=6, sticky=W+E)


        self.searchbtn = ttk.Button(self.frame, padding=(3,8), text=txt['search'], state='disable')
        self.searchbtn.grid(row=0, column=6, columnspan=2, sticky=W+E)

        self.clearSearch = ttk.Button(self.frame, padding=(1,8), text=txt['clear'], state='disable')
        self.clearSearch.configure(command=cb.onclearsearch)
        self.clearSearch.grid(row=0,column=8)

    def buildCategores(self):
        panelfile = open("./panel.json")
        self.panel = json.load(panelfile)

        self.categores = list()

        for index, cname in enumerate(categoryorder):
            cat = ttk.Button(self.frame, text=cname[1])
            cat.grid(row=1, column=index)
            self.categores.append(cat)        

    def mainloop(self):
        self.root.mainloop()
