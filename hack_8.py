"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = []
    num = 1
    for i in s:
        result.insert(0, f"{num}" if len(s) % 2 == 0 else f"{i}-{num}")
        num += 1   
    return result
