import os
import colorama
from colorama import *
import termcolor
from termcolor import *
from ColorsT import *
colorama.init(autoreset=True)

print('\033[31m' + 'some red text')
print('\033[39m')  # and reset to default color
print()
print(f"{Fore.RED}C{Fore.GREEN}O{Fore.YELLOW}L{Fore.BLUE}O{Fore.MAGENTA}R{Fore.CYAN}S{Fore.WHITE}!")
print(f"{Fore.RED}Red Text")
print(f"{Fore.GREEN}Green Text")
print(f"{Fore.YELLOW}Yellow Text")
print(f"{Fore.BLUE}Blue Text")
print(f"{Fore.MAGENTA}Magenta Text")
print(f"{Fore.CYAN}Cyan Text")
print(f"{Fore.WHITE}White Text")
print()
print(f"{Back.RED}B{Back.GREEN}A{Back.YELLOW}C{Back.BLUE}K{Back.MAGENTA}G{Back.CYAN}R{Back.WHITE}O{Back.RED}U{Back.GREEN}N{Back.YELLOW}D{Back.BLUE}!")
print(f"{Back.RED}Red Background")
print(f"{Back.GREEN}Green Background")
print(f"{Back.YELLOW}Yellow Background")
print(f"{Back.BLUE}Blue Background")
print(f"{Back.MAGENTA}Magenta Background")
print(f"{Back.CYAN}Cyan Background")
print(f"{Back.WHITE}White Background")
print()
print(f"{Style.DIM}S{Style.NORMAL}T{Style.BRIGHT}Y{Style.DIM}L{Style.NORMAL}E{Style.BRIGHT}!")
print(f"{Style.DIM}Dim Text")
print(f"{Style.NORMAL}Normal Text")
print(f"{Style.BRIGHT}Bright Text")
print()
print(f"{Fore.YELLOW}{Back.RED}C{Back.GREEN}{Fore.RED}O{Back.YELLOW}{Fore.BLUE}M{Back.BLUE}{Fore.BLACK}B{Back.MAGENTA}{Fore.CYAN}I{Back.CYAN}{Fore.GREEN}N{Back.WHITE}A{Back.RED}T{Back.GREEN}I{Back.YELLOW}O{Back.BLUE}N")
print(f"{Fore.GREEN}{Back.YELLOW}{Style.BRIGHT}Green Text - Yellow Background - Bright")
print(f"{Fore.CYAN}{Back.WHITE}{Style.DIM}Cyan Text - White Background - Dim")



COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
#You can add more colors and backgrounds to the dictionary if you like.


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


#Example printing out some text
hello = "[[red]]hello [[blue]]world[[white]]"
print(colorText(hello))


# BARRA DE PROGRESSO SHOW
import time

from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.styles import Style

style = Style.from_dict(
    {
        "title": "#4444ff underline",
        "label": "#ff4400 bold",
        "percentage": "#00ff00",
        "bar-a": "bg:#00ff00 #004400",
        "bar-b": "bg:#00ff00 #000000",
        "bar-c": "#000000 underline",
        "current": "#448844",
        "total": "#448844",
        "time-elapsed": "#444488",
        "time-left": "bg:#88ff88 #000000",
    }
)

"""
def main():
    with ProgressBar(style=style, title="Progress bar example with custom styling.") as pb:
        for i in pb(range(1600), label="Downloading..."):
            time.sleep(0.01)


if __name__ == "__main__":
    main()
"""