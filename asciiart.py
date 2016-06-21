from blocks import font

def prettyPrint(font,text):
    for i in range(font['height']):
        line=""
        for c in text:
            if c in font:
                line += font[c][i]
        print line

def prettyPrintCR(font,text,width=120):
    charsPerLine=width/font['width']
    nblines=(len(text)+charsPerLine-1)/charsPerLine
    for l in range(nblines):
        line=text[l*charsPerLine:(l+1)*charsPerLine]
        prettyPrint(font,line)

text = raw_input('Enter text:\n')
prettyPrintCR(font,text)
