
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
    def callback():
        w.emojis.destroy()
        w.buildPanel(cname[0])

    return callback    