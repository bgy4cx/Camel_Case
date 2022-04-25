from StrToCamelCase import *

def test_IsItStr_true():
    assert IsItStr('the-stealth-warrior') == True

def test_IsItStr_false():
    assert IsItStr(1234) == False

