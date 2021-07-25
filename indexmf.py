#-*- coding: -utf8 -*-
########## IMPORTS INI ##########       By. ( FoxPop / FabioCesar )
import os                       #1 
import sys                      #2 
from classMF.packMF import *    #3 - Todas as funções puras para o Software / dentro da pasta classMF --> arquivo packMF.py
#from mfglobal import *         #4 - Todas as variaveis global ficam nesse arquivo separado, localizado na pasta raiz do projeto --> arquivo mfglobal.py
######### IMPORTS END ###########  

while True:
    os.system("cls")
    Menuo()  # ------> @Menuo Inicia o programa Menu Principal
 




""" 
    [Pacote de Funções]
- Conjunto das principais funções criadas puras para o software.

INI --> Todas as funções criadas na pasta --> classMF --> packMF.py
@ Teste --------> Somente para testes rápidos
@ ListaPlayer --> Chama lista de Jogadores cadastrados com id
@ MenuLM -------> --> Menu Cadastro <-- sem interatividade cadastro, remover, buscar, lista, Jogadores
@ Escolha ------> Local para interagir com opções do Menu Principal ( if ).
@ MenuCad ------> Escolhas do @MenuLM ( if )/ MENU cadastro, remover, buscar, lista, Jogadores
@ Menuo --------> --> Menu Principal <-- Parte grafica do menu sem interatividade. Chama automáticamente a função @Escolha <--
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