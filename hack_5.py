"""
generic script

text: "fooziman" output => "fo-zi-ma-"
text: "barziman" output => "ba-zi-an"
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    palabra = list(s)
    vowels = ['a','e','i','o','u']
    longitud = len(palabra)
    if  longitud > 2:
        for i in palabra:
            if palabra[2] in vowels:
                palabra.insert(5,'-')
                palabra[2]='-'
                palabra[8]='-'
            elif palabra[2] not in vowels and longitud >= 5: 
                palabra[2] = '-'
                palabra[5] = '-'
            elif palabra[2] not in vowels and longitud <= 5:
                palabra[2] = '-'
    palabra = ''.join(palabra)
    return palabra