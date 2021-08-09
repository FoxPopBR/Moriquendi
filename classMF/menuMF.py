########## IMPORTS INI ##########
#from ast import Try            #1
#from mfglobal import *         #2
#import classMF
#from barLoad import BarM1
import colorama
from classMF.barLoad import BarM1
#import classMF.barLoad 
import os                       #3
import sys                      #4
from time import time,sleep     #5
from colorama import init, Fore, Style
#import termcolor
import time                     #7
from prompt_toolkit.output import ColorDepth
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.shortcuts.progress_bar import formatters
from prompt_toolkit.shortcuts.prompt import confirm
from termcolor import colored
#from termcolor import colored, cprint
######### IMPORTS END ###########
#colorama.init()

#colorama.init(autoreset=True)

# Abrir Castelo txt na tela ######
arqCas = open("C:/Git/Moriquendi/classMF/xtFile/castle.txt","r")
castle = arqCas.read             #
##################################

# Abir Logo MF Ascii na tela #####

arqMF = open("C:/Git/Moriquendi/classMF/xtFile/mfAscii.txt","r")
mfAscii = arqMF.read             #

##################################

# Abir Logo MF Ascii na tela #####
menuIN = open("C:/Git/Moriquendi/classMF/xtFile/Menuinicial.txt","r")
menuINI = menuIN.read             #
##################################


def MenuStart(): #Chama Logo Moriquendi - Castelo Desenhado e Menu Inicial com opções
    #colorama.init(autoreset=True)
    #init()
    #color_depth = ColorDepth.DEPTH_24_BIT
    os.system("cls")
    #print(f"{Fore.YELLOW}"+mfAscii)
    print("Fore.YELLOW [" + colored("green")+mfAscii,"]")
    arqCas.close
    print(castle())
    arqMF.close
    print("\n")
    BarM1()    # ------> #Chama uma barra de carregamento
    #sleep(1)
    #os.system("cls")
   # print(f"{Fore.YELLOW}"+mfAscii())
    #print(castle())
    #arqCas.close
    print("\n")
    print(menuINI())
    menuIN.close
    print("\n")
    return(input("Numero: "))


        
            