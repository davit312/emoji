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

        self.currentEmoji = ('', 0)
        self.emojiBarText = StringVar()
        self.emojiCode = StringVar()

        self.content = ttk.Frame(self.root)
        self.content.grid(column=0, row=0)

        self.frame = ttk.Frame(self.content, borderwidth=5,)
        self.frame.grid(column=0, row=0, columnspan=8, rowspan=4)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font='Drooid 16')
        self.style.configure('Category.TButton', foreground='#192754', bordercolor='#192734')
        self.style.configure('TEntry', font="Droid 16")

        self.canvas = VerticalScrolledFrame(self.frame)
        self.canvas.grid(row=2, column=0, columnspan=10, sticky=W+E)
        self.canvas.bind('<Leave>', cb.onPanelLeave)

    def build(self):
        self.buuildTopBar()
        self.buildCategores()
        self.buildPanel('people')
        self.buildFooter()

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
                            text=category[1],
                            style='Category.TButton')
            cat.grid(row=1, column=index)
            cat.bind('<Enter>', cb.createCategoryHover(category))
            self.categores.append(cat) 

    def buildPanel(self, catname):

        r = c = 0 

        self.emojis = ttk.Frame(self.canvas, height=400)
        self.emojis.grid(row=0, column=0)

        for i in self.panel[catname]:
            btn = ttk.Button(self.emojis, text=emoji[i][0],
                            command=cb.createEmojiClick(emoji[i],i),
                            style='Emoji.TButton')
            btn.bind('<Enter>', cb.createEmojiHover(i))

            btn.grid(row=r, column=c)
            c += 1
            if c == 9:
                c = 0
                r += 1

    def buildFooter(self):
        self.emojiname = ttk.Label(self.frame,textvariable=self.emojiBarText, font=("", 16))        
        self.emojiname.grid(row=3, column=0, columnspan=9)

        self.copyBar = ttk.Entry(self.frame, 
                                textvariable=self.emojiCode,
                                font=("", 16) )

        self.copyBar.grid(row=4, column=0, columnspan=2, sticky=W)

        ttk.Button(self.frame, 
                command=cb.onCopyButton,
                text=txt['copy']).grid(row=4,column=2)

    def buildEmojibar(self, emojiIndex):
        self.emojiBarText.set(formatEmName(emoji[emojiIndex][1]))

    def resetEmojibar(self):
        if self.currentEmoji[1] == 0:
            return self.emojiBarText.set('')    
        self.emojiBarText.set(formatEmName( emoji[ self.currentEmoji[1] ][1] ) )

    def mainloop(self):
        self.root.mainloop()


def formatEmName(emname):
    return emname[0].upper() + emname[1:].replace('_', ' ')