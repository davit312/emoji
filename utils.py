from os.path import exists
import json

from vars import recentUsedPath

def filterQuery(query):
    q = query.strip().replace(' ','_')
    return q

def calculateTwemojiCode(symbol):
    isnumeric = False
    result = ''

    for index, char in enumerate(symbol):
          
        code = ord(char)

        # *, #, 0-9 numbers 
        if index == 0 and code < 0x40:
            isnumeric = True
        if isnumeric and index == 1:
            continue 

        if index != 0:
            result += '-'  
        
        result +=  "{:x}".format(code)
    
    return result

def getRecent():
    recent = []
    if not exists(recentUsedPath):
        return recent
    else:
        with open(recentUsedPath, 'r') as rec:
            return json.load(rec)

def addToPanel(emojiIndex, recent):
    if emojiIndex in recent:
        recent.remove(emojiIndex)
    
    recent.append(emojiIndex)
    
    length = len(recent)

    if length > 30:
        print(547)
        recent.pop(0)

def saveRecentUsed(recent):
    recentJson = json.dumps(recent)

    with open(recentUsedPath, 'w') as rec:
        rec.write(recentJson)