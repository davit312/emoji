import time
import tkinter
from threading import Timer
import pyperclip

from vars import *
from data.emoji import *
from utils import *


def setWindow(windowObject):
    global w
    w = windowObject

lastPress = 0

def dosearch(minSearchLen = SearchStarting):
    now = round(time.time() * 1000)

    if (now - lastPress) < 1500:
        return

    rawQuery = w.search.get()
    query = filterQuery(rawQuery)
    queryLength = len(query)

    if queryLength > 0:
        w.searchbtn.state(['!disabled'])
        w.clearSearch.state(['!disabled'])
    else:
        w.searchbtn.state(['disabled'])
        w.clearSearch.state(['disabled'])
        return
    
    if queryLength < minSearchLen:
        return

    result = list()
    
    index = 0
    for emj in emoji:
        for etext in emj[1:]:
            if query in etext:
                result.append(index)
                continue
        index += 1
    
    try:          
        w.emojis.destroy()
    except tkinter.TclError:
        print('Error in tkinter')

    if len(result) > 0:
        w.buildPanel('', result)
    else:
        w.buildNotFound()

    w.buildRawSearchText(rawQuery)

def onsearch(*args):
    global lastpress
    lastPress = round(time.time() * 1000)

    searchTimeout = Timer(1.3, dosearch)
    searchTimeout.start()

def onclearsearch():
    w.search.set('')
    w.searchbar.focus()

def crateonpressCategory(cname):
    def oncategorypress():
        w.emojis.destroy()
        w.currentEmoji = DefaultEmoji
        footertxt = w.emojiBarText.get()
        w.emojiBarText.set(footertxt)
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
    if len(w.currentEmoji[0]) == 0:
        return print('Nothing to copy!')
    pyperclip.copy(w.currentEmoji[0][0])

def onTwemojiClick(*args):
    if len(w.currentEmoji[0]) == 0:
        return print('Nothing to copy!')

    twemojiCode = calculateTwemojiCode(w.currentEmoji[0][0])

    result = CDN["url"]
    
    imgType = w.imageType.get()

    if imgType == "0":
        result += CDN["png"] + twemojiCode + ".png"
    else:
        result += CDN["svg"] + twemojiCode + ".svg"

    w.twemojiCode.set(result)    
    pyperclip.copy(result)
