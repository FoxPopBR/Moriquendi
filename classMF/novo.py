from colorama import init, Fore, Style
init()

# by Colorama’s constant shorthand for ANSI escape sequences:
# -----------------------------------------------------------
from colorama import Fore, Back, Style
print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color

# by manually printing ANSI sequences from your own code:
# -------------------------------------------------------
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

# by using your code sample
# -------------------------
green = Fore.GREEN
print(f'{green}This is a test')