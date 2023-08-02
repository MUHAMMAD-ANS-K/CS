from pyfiglet import Figlet
import sys

font = Figlet()
font.getFonts()

if len(sys.argv) == 1:
    font.setFont(font = 'slant')
elif len(sys.argv) == 3:
    font.setFont(font = sys.argv[2])
else:
    sys.exit('Invalid usage')
s = input('Input: ')
print('Output:')
print (font.renderText(s))