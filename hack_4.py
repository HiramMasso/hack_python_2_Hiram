"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    deleted = {'f': '', 'b': '', 'n': ''}
    result = ''.join(deleted.get(caracter, caracter) for caracter in s)
    return result
