# This function verify the string variable. 
from cgitb import text


def IsItStr(text):
    return isinstance(text, str)

# This function convert the string to camel case. If the variable is not string, the result is an empty string. 
def To_Camel_Case(text):
    if isinstance(text, str):
        ctext = ''
        for x in range(len(text)):
            if text[x] == '-' or text[x] == '_':
                ctext=ctext + str(text[x+1].upper())
            elif text[x-1] == '-' or text[x-1] == '_':
                continue
            else:
                ctext=ctext + str(text[x])
    else: ctext = ''
    return ctext
