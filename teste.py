# -*- coding: -utf8 -*-
""" [TESTES / summary]
- Local para chamadas de teste do dev.
- Iniciar aqui uma plataformar automática para teste do Software.
- Criar um menu agradavel para receber e apresentar os dados dos testes.
- Notas maiores de Modificação ou adaptação do projeto deve ser feritas aqui!

    [extended_summary]
    *Aguardando Versionamento 1.0.1*
By. ( FoxPop / FabioCesar )
"""
# Importa pacote de funções e variáveis criados em pastas separadas!
########## IMPORTS INI ########## 

from classMF.packMF import *    #1 - Todas as FUNÇÕES puras para o Software / dentro da pasta classMF --> arquivo packMF.py
from classMF.menuMF import BarraLoadM
#from mfglobal import *         #2 - Todas as VARIÁVEIS global ficam nesse arquivo separado, localizado na pasta raiz do projeto --> arquivo mfglobal.py
######### IMPORTS END ###########
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

#   Chamada de Funções para teste


print(BarraLoadM())




#while True:
 #  MenuLM()

"""

import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    print(i,'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

"""



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

By. ( FoxPop / FabioCesar )
"""