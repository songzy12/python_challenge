# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request
import re

URL_ROOT = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def get_next_nothing(nothing):
    url = URL_ROOT + nothing
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
    
    # Extract the next 'nothing' number from the response
    match = re.search(r'and the next nothing is (\d+)', html)
    if match:
        return match.group(1)
    else:
        print(html)

def run(nothing):
    print("  ", nothing)
    while True:
        nothing = get_next_nothing(nothing)
        if not nothing:
            break
        print("->", nothing)

if __name__ == "__main__":
    nothing = "12345"
    # -> 3875
    # -> 16044
    # Yes. Divide by two and keep going.

    nothing = f"{16044//2}"
    # -> 52899
    # -> 66831
    # peak.html
    run(nothing)
