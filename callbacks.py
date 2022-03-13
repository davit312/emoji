from threading import Timer
import pyperclip

from emoji import *
from utils import *


def setWindow(windowObject):
    global w
    w = windowObject

def onsearch(*args):
    if w.lockSearch:
        return

    w.lockSearch = True

    def dosearch():
        
        searchText = w.search.get()

        if len(searchText) > 0:
            w.searchbtn.state(['!disabled'])
            w.clearSearch.state(['!disabled'])
        else:
            w.searchbtn.state(['disabled'])
            w.clearSearch.state(['disabled'])
        

        query = filterQuery(searchText)
        result = list()

        w.emojis.destroy()        
        if len(result) > 0:
            w.buildPanel('', result)
        else:
            w.buildNotFound()
        
        w.lockSearch = False


    searchTimeout = Timer(0.8, dosearch)
    searchTimeout.start()

def onclearsearch():
    w.search.set('')
    w.searchbar.focus()

def crateonpressCategory(cname):
    def oncategorypress():
        w.emojis.destroy()
        w.buildPanel(cname[0])

    return oncategorypress    


def createCategoryHover(category):
    def oncategoryHover(event):
        catText = category[1] + " " + category[2]
        w.emojiBarText.set(catText)
    
    return oncategoryHover

def createEmojiHover(symbolIndex):
    def onemojihover(event):
        w.buildEmojibar(symbolIndex)

    return onemojihover

def createEmojiClick(emj, index):

    def onbuttonclick():
        w.currentEmoji = (emj, index)
        w.emojiCode.set(w.currentEmoji[0][0])

    return onbuttonclick


def onPanelLeave(e):
    w.resetEmojibar()


def onCopyButton():
    pyperclip.copy(w.currentEmoji[0][0])
