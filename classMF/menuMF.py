########## IMPORTS INI ##########
#from ast import Try            #1
#from mfglobal import *         #2
#import classMF
import os                       #3
import sys                      #4
from time import time,sleep     #5
from colorama import *          #6
import colorama                 #7
from termcolor import *         #8
import time
from prompt_toolkit.output import ColorDepth
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.shortcuts.progress_bar import formatters
from prompt_toolkit.shortcuts.prompt import confirm
from classMF.barLoad import BarM1
from classMF.barLoad import *

######### IMPORTS END ###########
colorama.init(autoreset=True)

# Abrir Castelo txt na tela ######
arqCas = open("classMF/xtFile/castle.txt","r")
castle = arqCas.read             #
##################################

# Abir Logo MF Ascii na tela #####
arqMF = open("/classMF/xtFile/mfAscii.txt","r")
mfAscii = arqMF.read             #
##################################

# Abir Logo MF Ascii na tela #####
menuIN = open("classMF/xtFile/Menuinicial.txt","r")
menuINI = menuIN.read             #
##################################


def MenuStart(): #Chama Logo Moriquendi - Castelo Desenhado e Menu Inicial com opções
    os.system("cls")
    print(f"{Fore.YELLOW}"+mfAscii())
    print(castle())
    BarM1()    # ------> #Chama uma barra de carregamento
    sleep(1)
    os.system("cls")
    print(f"{Fore.YELLOW}"+mfAscii())
    print(castle())
    print(menuINI())
    return(input("Numero: "))


        
            