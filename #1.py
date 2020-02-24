def find_message(text: str) -> str:
    """Find a secret message"""
    import re
    a=""
    x=str(text)
    y=x.upper()
    #x=x.replace(" ","").replace(".","").replace(",","").replace("?","").replace("!","")
    #y=y.replace(" ","").replace(".","").replace(",","").replace("?","").replace("!","")
    x = re.sub('[!,-= .*&#/?:$}]', '', x)
    y = re.sub('[!,-= .*&#/?:$}]', '', y)
    
    for i in zip(x,y) :
        if i[0] == i[1] :
            a = a+i[0]
        else : 
            continue
    return (a)