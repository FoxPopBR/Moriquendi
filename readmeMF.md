#-*- coding: -utf8 -*-
""" 
    [>> Organograma Moriquendi INI <<]
My first study version of Python.       By. ( FoxPop / FabioCesar )

    Versionamentos Prontos

--> MF_vs_1.0.1 data 
--> MF_vs_1.0.0 data 07/21/2021

lasted update >> *18:00 date 07/24/2021* <<

Initial scope of the project:

Control of members with registrations of players and guild activities, manipulation of registered data. Innovations in the project scope and implementations of new technologies and API's!



Version 1.0.1 
( 1 / 6 )

2.1 Registration of Mobs and Events types 
o---------------------------------------------------- [  ]
2.2 Add colors,sounds and ASCII drawings to Menus
o---------------------------------------------------- [  ]
2.3 Implements for Excel 
o---------------------------------------------------- [  ]
2.4 Receive data from a website and store it
o---------------------------------------------------- [  ]
2.5 Create a framework for automated Mob couting 
o---------------------------------------------------- [  ]
2.6 Create a window on Windows to display the code
o---------------------------------------------------- [  ]

*********************************************************** 
Version 1.0.0 ( 10 / 10 ) --------\o/*18:00 date 07/24/2021* Complete *                                                         
1. Player list 
---------------------------------------------------o [ OK ]
2. Consult player names, number of members
---------------------------------------------------o [ OK ]
3. Exit button
---------------------------------------------------o [ OK ]
4. Add comments in clean and objective correct throughout the code! 
---------------------------------------------------o [ OK ]
5. Add and remove name player 
---------------------------------------------------o [ OK ]
6. Display player names in alphabetical list, with and id number as numeric identification 
---------------------------------------------------o [ OK ]
7. Add and remove name player 
---------------------------------------------------o [ OK ]
8. Display player names in alphabetical list, with and id number as numeric identification 
---------------------------------------------------o [ OK ]
9. Review and test all code!
---------------------------------------------------o [ OK ]
10. Create separate files for (functions/global variables/visual part/index) 
---------------------------------------------------o [ OK ]
***********************************************************

The entire repository created and managed by the Git terminal. Material "codado" in VScode.

By. ( FoxPop / FabioCesar )

    [>> Organograma Moriquendi END <<]

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
