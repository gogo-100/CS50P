from pyfiglet import Figlet
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    str = input("Input: ")
    print("Output: ")
    print(figlet.renderText(str))
elif len(sys.argv) == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--f':
        sys.exit("<-f / --f> <font name>")
    str = input("Input: ")
    print("Output: ")
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(str))
    except:
        sys.exit("font name error")
else:
    sys.exit("need 0 or 2arguments")