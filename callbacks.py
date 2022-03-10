
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