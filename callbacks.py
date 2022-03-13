
def setWindow(windowObject):
    global w
    w = windowObject

def onsearch(*args):
    searchText = w.search.get()

    if len(searchText) > 0:
        w.searchbtn.state(['!disabled'])
        w.clearSearch.state(['!disabled'])
    else:
        w.searchbtn.state(['disabled'])
        w.clearSearch.state(['disabled'])

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

def createEmojiClick(emoji):

    def onbuttonclick():
        print(emoji)

    return onbuttonclick