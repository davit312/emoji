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