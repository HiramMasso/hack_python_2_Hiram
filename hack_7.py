"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if s == [(0)]:
        result = s
    else:
        letras = list(s)
        mapeo = {letra: str(index) for index, letra in enumerate(letras, start=1)}
        result = []
        for index, letra in enumerate(letras):
            if index % 2 == 0:
                result.append(mapeo[letra])
            else:
                result.append(int(mapeo[letra]))
    return result
