def find_message(text: str) -> str:
    """Find a secret message"""
    a = ""
    x = str(text)
    y = x.upper()
    for i,j in x,y :
        if i == j :
            a=a+j
        else :
            continue
    return a
