"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    reemplazos = {
        'a': '@',
        'o': '0',
        'f': 'F',
        'n': 'N',
        'i': '¡',
        'q': 'Q',
        'u': 'v',
        'x': 'X',
        'b': 'B'
    }
    
    result = ''.join(reemplazos.get(caracter, caracter) for caracter in s)
    return result