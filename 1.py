# http://www.pythonchallenge.com/pc/def/map.html

import string

# m = {'k':'m', 'o':'q', 'e': 'g'}


def build_m():
    m = {}
    letters = string.ascii_lowercase
    for i in range(len(letters)):
        m[letters[i]] = letters[(i+2) % (len(letters))]
    return m


def map_text(text, m):
    return ''.join(map(lambda x: m.get(x, x), list(text)))


m = build_m()
original_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(map_text(original_text, m))

print(map_text('map', m))
