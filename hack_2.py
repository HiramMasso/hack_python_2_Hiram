"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vowels = ["a","e","i","o","u"]
    _str = []
    
    for txt in result:
        if txt not in vowels:
          _str.append(txt)  
          
    result = "".join(_str)
    return result 

#Llamar a la función con un ejemplo
input_string = "hola mundo"
output_string = fn_hack_2(input_string)

#Mostrar el resultado
print("Cadena original:", input_string)
print("Cadena sin vocales:", output_string)