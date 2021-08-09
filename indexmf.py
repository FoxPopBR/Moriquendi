#-*- coding: -utf8 -*-
########## IMPORTS INI ##########       By. ( FoxPop / FábioCesar )
#import classMF
from classMF.menuMF import MenuStart
#from classMF.packMF import *
from classMF.barLoad import *
from classMF.callMF import *
#from classMF.packMF import *
#from classMF import barLoad,packMF,menuMF,callMF
import os                       #1 
import sys
from colorama import init, Fore, Style
init()
#import classMF.packMF MenuStart
######### IMPORTS END ###########  
#colorama.init(autoreset=True)

while 1:
    init()
    os.system("cls")
    MenuStart()  # ------> #Chama Logo Moriquendi e Castelo Desenhado
    exit()




""" 
    [Pacote de Funções]
- Conjunto das principais funções criadas puras para o software.

INI --> Todas as funções criadas na pasta --> classMF --> packMF.py
@ Teste --------> Somente para testes rápidos
@ ListaPlayer --> Chama lista de Jogadores cadastrados com id
@ MenuLM -------> --> Menu Cadastro <-- sem interatividade cadastro, remover, buscar, lista, Jogadores
@ Escolha ------> Local para interagir com opções do Menu Principal ( if ).
@ MenuCad ------> Escolhas do @MenuLM ( if )/ MENU cadastro, remover, buscar, lista, Jogadores
@ Menuo --------> --> Menu Principal <-- Parte gráfica do menu sem interatividade. Chama automáticamente a função @Escolha <--
FIM <-- Todas as funções criadas em <-- classMF

    [Variável Global]
- Conjunto de variáveis global separado no arquivo --> mfglobal.py / pasta raiz

INI --> Variáveis Global -->
- NomePlayer  --> Lista de jogadores cadastrados
- qt          --> Quantidade de jogadores cadastrados
- contador    --> Quantidade de opções escolhidas "controle dev"
- IdJogador   --> Numeros de 1 a 100 / Referência ID para jogadores cadastrados
FIM <-- Variáveis Global <--

By. ( FoxPop / FábioCesar )
"""
