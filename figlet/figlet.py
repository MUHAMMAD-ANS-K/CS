from pyfiglet import Figlet
import sys

font = Figlet()
font = font.getFonts()
font = font.setFont(font = 'slant')
# if len(sys.argv) == 1:
 #  font = Figlet(font = 'slant')
#elif len(sys.argv) == 3:
 #   font = Figlet(font = sys.argv[1] + sys.argv[2])
#else:
 #   sys.exit('Invalid usage')

print (font.renderText('render'))