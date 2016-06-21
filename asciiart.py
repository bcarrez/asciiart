import sys
from blocks import font

def prettyPrint(font,text):
    for i in range(font['height']):
        line=""
        for c in text:
            if c in font:
                line += font[c][i]
        print line

text = sys.argv[1]
prettyPrint(font,text)
