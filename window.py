from tkinter import *
from tkinter import ttk

import json

from VerticalScrolledFrame import *

from emoji import *
from vars import *
import callbacks as cb

class root():

    def __init__(self):
        cb.setWindow(self)

        with open("./panel.json") as panelfile:
            self.panel = json.load(panelfile)
            self.panel['recent'] = []

        self.root = Tk()
        self.root.title(txt['title'])

        self.content = ttk.Frame(self.root)
        self.content.grid(column=0, row=0)

        self.frame = ttk.Frame(self.content, borderwidth=5,)
        self.frame.grid(column=0, row=0, columnspan=8, rowspan=4)

        self.canvas = VerticalScrolledFrame(self.frame)

        self.canvas.grid(row=2, column=0, columnspan=10, sticky=W+E)
   
    def build(self):
        self.buuildTopBar()
        self.buildCategores()
        self.buildPanel('people')
        self.buildFooter

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

        self.categores = list()

        for index, category in enumerate(categoryorder):
            cat = ttk.Button(self.frame, 
                            command=cb.crateonpressCategory(category),
                            text=category[1])
            cat.grid(row=1, column=index)
            self.categores.append(cat) 

    def buildPanel(self, catname):

        r = c = 0 

        self.emojis = ttk.Frame(self.canvas, height=300)
        self.emojis.grid(row=0, column=0)
    
        for i in self.panel[catname]:
            ttk.Button(self.emojis,text=emoji[i][0]).grid(row=r, column=c)
            c += 1
            if c == 9:
                c = 0
                r += 1

    def buildFooter(self):
        pass

    def mainloop(self):
        self.root.mainloop()
