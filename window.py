from sre_parse import expand_template
from tkinter import *
from tkinter import ttk

import json

from VerticalScrolledFrame import *

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
        self.buildPanel()

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

    def buildPanel(self):
        
        canvas = VerticalScrolledFrame(self.frame)

        canvas.grid(row=2, column=0, columnspan=10, sticky=W+E)

        self.emojis = ttk.Frame(canvas, height=300)
        self.emojis.grid(row=0, column=0)
    
        for j in range(50):
            for i in range(9):
                ttk.Button(self.emojis,text=str(j)+" " + str(i)).grid(row=j, column=i)

   



    def mainloop(self):
        self.root.mainloop()
