def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    uptext = text.upper()
    ctext = text.capitalize()
#   for i in text : 
    if text[0] == uptext[0] : 
        pass
    else : 
        text = uptext[0]+text[1:]    
            
    if text.endswith('.') == True : 
        pass
    else : 
        text = text + '.'
        # your code here
    return text

# print(correct_sentence("Polved, correct"))
