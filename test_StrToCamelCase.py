from StrToCamelCase import *

def test_IsItStr_true():
    assert IsItStr('the-stealth-warrior') == True

def test_IsItStr_false():
    assert IsItStr(1234) == False

def test_To_Camel_Case_1():
    assert To_Camel_Case('The_Stealth_Warrior') == 'TheStealthWarrior'

def test_To_Camel_Case_2():
    assert To_Camel_Case('the-stealth-warrior') == 'theStealthWarrior'

def test_To_Camel_Case_3():
    assert To_Camel_Case(1234) == ''