import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
# ^^^ part of the figlet usage

#get input from user
fonts = figlet.getFonts()
try:

    #if command line index 1 is  -f or --font do...
    if sys.argv[1] == "-f" and sys.argv[2] in fonts:
        input = input("Input: ")
        fontName = sys.argv[2]
        figlet.setFont(font= fontName)
        print(figlet.renderText(input))

    elif sys.argv[1] == "--font" and sys.argv[2] in fonts:
        input = input("Input: ")
        fontName = sys.argv[2]
        figlet.setFont(font= fontName)
        print(figlet.renderText(input))

    else:
        print("Invalid usage")
        sys.exit(1)




except IndexError:
    input = input("Input: ")
    randomFont = random.choice(figlet.getFonts())
    figlet.setFont(font= randomFont)
    print(figlet.renderText(input))
