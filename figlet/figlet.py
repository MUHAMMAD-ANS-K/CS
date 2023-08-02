from pyfiglet import Figlet
import sys

font = Figlet()
font.getFonts()

if len(sys.argv) == 1:
    font.setFont(font = 'slant')
elif len(sys.argv) == 3:
    try:
        font.setFont(font = sys.argv[2])
    except FontNotFound(font):
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')
s = input('Input: ')
print('Output:')
print (font.renderText(s))