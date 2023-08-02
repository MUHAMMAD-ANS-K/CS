from pyfiglet import Figlet
import sys

if len(sys.argv) == 1:
    font = Figlet(font = 'slant')
elif len(sys.argv) == 3:
    font = Figlet(font = argv[1] + argv[2])
else:
    sys.exit('Invalid usage')

print (renderText('render'))