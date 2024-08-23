"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    num = 0
    for item in s:
        num += 1
        if type(item) == dict:
            result.append({str(num): str(num + 1)})
        elif type(item) == set:
            result.append({str(num), str(num + 1)})
        num += 1
    return result

print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]))