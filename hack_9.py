"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    for key, value in s.items():
        if key == 'foo':
            result[key.title()] = value.replace('k', '').capitalize()
    return result
