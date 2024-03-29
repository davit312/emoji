from tkinter import *
from tkinter import ttk

from VerticalScrolledFrame import *

from data.emoji import *
from data.panel import *
from vars import *
import callbacks as cb
import utils


class root():

    def __init__(self):
        cb.setWindow(self)

        self.panel = panel
        self.panel['recent'] = utils.getRecent()

        self.root = Tk()
        self.root.title(txt['title'])

        self.lockSearch = False
        self.currentEmoji = DefaultEmoji
        self.emojiBarText = StringVar()
        self.emojiCode = StringVar()
        self.imageType = StringVar(value=0)

        self.content = ttk.Frame(self.root)
        self.content.grid(column=0, row=0)

        self.frame = ttk.Frame(self.content, borderwidth=5,)
        self.frame.grid(column=0, row=0, columnspan=8, rowspan=4)

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('TButton', font='Drooid 16')
        self.style.configure('Twemoji.TButton', font=('Droid 12'),)

        self.style.configure('Category.TButton', foreground='#192754',)

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
        self.searchbar.grid(row=0, column=0, columnspan=6, sticky=W+E)

        self.searchbar.bind('<Return>', lambda event: cb.dosearch(0))

        self.searchbtn = ttk.Button(self.frame, 
                        command=lambda: cb.dosearch(0), 
                        padding=(3,8), text=txt['search'], state='disable')
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
            cat.grid(row=1, column=index, sticky=W)
            cat.bind('<Enter>', cb.createCategoryHover(category))
            self.categores.append(cat)

    def buildPanel(self, catname, otherEmojis = None):

        r = c = 0 

        self.emojis = ttk.Frame(self.canvas, height=400)
        self.emojis.grid(row=0, column=0)

        if otherEmojis == None:
            emojis = self.panel[catname]
            if catname == 'recent':
                emojis = emojis.copy()
                emojis.reverse()
        else:
            emojis = otherEmojis

        for i in emojis:
            btn = ttk.Button(self.emojis, text=emoji[i][0],
                            command=cb.createEmojiClick(emoji[i],i),
                            style='Emoji.TButton')
            btn.bind('<Enter>', cb.createEmojiHover(i))

            btn.grid(row=r, column=c)
            c += 1
            if c == 9:
                c = 0
                r += 1

    def buildNotFound(self):
        self.emojis = ttk.Frame(self.canvas,)
        self.emojis.grid(row=0, stick=W+E)

        nf = ttk.Label(self.emojis, text=txt['notfound'])
        nf.grid(row=0, column=0, stick=W+E)

    def buildFooter(self):
        self.emojiname = ttk.Label(self.frame,textvariable=self.emojiBarText, font=("", 16))        
        self.emojiname.grid(row=3, column=0, columnspan=9)

        twemojiRow = ttk.Frame(self.frame,)
        twemojiRow.grid(row=5, column=0, columnspan=9, pady=(10, 0), sticky=W+E)

        self.copyBar = ttk.Entry(twemojiRow, textvariable=self.emojiCode, font=("", 12) )

        self.copyBar.grid(row=0, column=0, sticky=W)

        copybtn = ttk.Button(twemojiRow, command=cb.onCopyButton,text=txt['copy'])
        copybtn.grid(row=0, column=1, padx=(5, 50))

        self.twemojiCode = StringVar()
        self.twemojiBar = ttk.Entry(twemojiRow, textvariable=self.twemojiCode, font=('Droid', 12))
        self.twemojiBar.grid(row=0, column=2, columnspan=2, sticky=W)

        rb = ttk.Radiobutton(twemojiRow, text="PNG", width=0, variable=self.imageType, value=0)
        rb.grid(row=0,column=4,padx=5,sticky=W)
        rb = ttk.Radiobutton(twemojiRow, text="SVG", width=0, variable=self.imageType, value=1)
        rb.grid(row=0,column=5,padx=5,sticky=W)

        cptw = ttk.Button(twemojiRow,text=txt['copy'] + " twemoji address", command=cb.onTwemojiClick, )
        cptw.grid(row=0, column=6, padx=10, sticky=E)

    def buildEmojibar(self, emojiIndex):
        self.emojiBarText.set(formatEmName(emoji[emojiIndex][1]))

    def resetEmojibar(self):
        if self.currentEmoji[1] == -2:
            return self.emojiBarText.set(self.currentEmoji[0])  
  
        if self.currentEmoji[1] == -1:
            return self.emojiBarText.set('')    
        self.emojiBarText.set(formatEmName( emoji[ self.currentEmoji[1] ][1] ) )

    def buildRawSearchText(self, rawQuery):
        self.currentEmoji =  (txt['resultFor'] + rawQuery, -2)
        self.emojiBarText.set(self.currentEmoji[0])

    def mainloop(self):
        self.searchbar.focus()

        self.root.protocol("WM_DELETE_WINDOW", cb.saveRecent)
        self.root.mainloop()


# helper function
formatEmName = lambda emname: emname[0].upper() + emname[1:].replace('_', ' ')