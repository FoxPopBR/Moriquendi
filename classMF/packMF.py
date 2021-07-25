# -*- coding: utf-8 -*-
""" [Bibliotecas - Pacotes de Funções]
- Aqui são criadas todas as funções e derivados

@ Teste --------> Somente para testes rápidos
@ ListaPlayer --> Gera lista de Jogadores cadastrados com id
@ MenuLM -------> Desenho do MENU sem interatividade cadastro, remover, buscar, lista, Jogadores
@ Escolha ------> Local para interagir com opções do menu, manipulação de variáveis e parte lógica da interface 
@ MenuCad ------> Escolhas do MenuLM / MENU cadastro, remover, buscar, lista, Jogadores
@ Menuo --------> Parte grafica do menu sem interatividade, chama automáticamente a função Escolha

    [extended_summary]
- Novas funções e derivadas serão criadas aqui!
By FoxPop / FabioCesar
    """
########## IMPORTS INI ##########
from ast import Try             #1
from mfglobal import *          #2
import os                       #3
import sys                      #4
from time import time,sleep     #5
######### IMPORTS END ###########

def Teste():         # ---> Nada aqui sómente para testes rápidos <---
    print("Local para teste")


def ListaPlayer():   # ---> Lista de jogadores com ID por ordem Alfabetica <---
    global NomePlayer,IdJogador,contador,qt,qt1
    os.system ("cls")
    qt = qt1 = len(NomePlayer)
    orList = sorted(NomePlayer,key=str.lower) # --> Organiza uma lista em ordem alfabetica <-- obs: chorei sangue aqui @.@
    for i in range(qt):      
        print("ID:",IdJogador[i]," ",orList[i])


def MenuLM():        # Desenho MENU Simple ---> Procurar Jogadores <---
    os.system("cls") #chama comando do sistema operacional, no caso o comando "cls"
    print("Iniciando treinamento Python\nProjeto controle Moriquendi Federation")
    print("===================================================================")
    print("==                                                               ==")
    print("==                    Moriquendi Federation                      ==")
    print("==                                                               ==")
    print("==  1- Procurar Jogador por Nome                                 ==")
    print("==  2- Procurar Jogador por ID                                   ==")
    print("==  3- Mostrar lista de jogador                                  ==")
    print("==  4- Add nome de Jogador                                       ==")
    print("==  5- Remover nome de Jogador                                   ==")
    print("==  6- Retornar ao menu principal                                ==")
    print("==                                                               ==")
    print("===================================================================\n")
    print("Opções escolhidas:",contador,"\n")
    

def Escolha():       # Opções de Menu Inicial
    global NomePlayer,IdJogador,contador # Variável precisa ser declarada dentro da função como global para ser modificada
    opcao = input("Escolha uma opção:") #Escolhendo uma opção no menu
    contador = contador + 1
    if opcao == "1":
        MenuCad()     
    elif opcao == "2":      # ------------> Continua a opção 2 do menu principal
        qt = qt1 = len(NomePlayer)
        print("Quantidade de membros da guild:",qt)     
        input("Enter P/ Continuar..")
        Menuo()
    elif opcao == "3": # Unico jeito de parar o programa é escolhendo a opção 3 do menu
        os.system("cls")
        print("Desligando e fechando tudo.")
        sleep(2)
        os.system("cls")
        print("Bye ,o/")
        sleep(1)
        quit()        
    else:   # Sempre que não digitar uma opção valida
        print("Você entendeu as opções? Faça direito!")
        print("Você digitou: "),opcao
        input("Enter P/ Continuar..")
        Menuo()


def MenuCad ():      # ---> MENU CADASTRO JOGADOR <---
    global NomePlayer,IdJogador,contador,qt # --> Variável global só pode ser chamada uma vez por def
    os.system("cls")
    MenuLM()
    digop = ""
    opcao = input("Escolha uma opção:") #Escolhendo uma opção no menu
    if opcao == "1":    # ---> Buscar Jogador DIGITANDO NOME <---
        digop = input("Buscar Nome:" )
        if digop in NomePlayer: # --> 
            print("O jogador:",digop,"SIM! é um membro da guild! \o/")
            input("Enter P/ Continuar..")   
            MenuCad()  
        else:
            print("O jogador:",digop,"NÃO! faz parte da guild! =s")
            input("Enter P/ Continuar..")
            MenuCad()
    elif opcao == "2":     # ---> Buscar Jogador por ID <---  
        os.system("cls")
        qt = qt1 = len(NomePlayer)
        orList = sorted(NomePlayer,key=str.lower)
        print("Digite o NUMERO ID do Jogador\n")
        try:    # --> Tente fazer isso até / except
            t1 = int(input())
        
            if t1 <= qt:
                t2 = t1 - 1
                print("ID:",t1," ",orList[t2])
                input("Enter para continuar...")
                MenuCad()
            else:
                print("Esse ID esta vazio, ou não existe!")    
                input("Enter para continuar..")
                MenuCad()
                os.system()     # <--
        except (TypeError,ValueError):  # ---> Caso try falhe com esses erros faça isso
            print("Coloque NUMERO do ID valido")    
            input("Enter para continuar..")
            MenuCad()   #<----
    elif opcao == "3":  # ---> Mostra Lista de jogadores com ID <---
        ListaPlayer()
        input("Enter P/ Continuar..")
        os.system("cls")
        MenuCad()
    elif opcao == "4":  # ---> ADD Nome de JOGADOR na LISTA <---
        nt = ""
        print("**************************************************************")
        print("*** Insira o nome do jogador a ser add na lista de membros ***")
        print("***                                                        ***")
        nt = input("Digite o nome:")
        NomePlayer.append(nt)
        print("Nome add:",nt)
        input("Enter para continuar")
        os.system("cls")
        print("**************************************************************")
        print("*** Insira o nome do jogador a ser add na lista de membros ***")
        print("***                                                        ***")
        print("Jogador",nt," foi adicionado com sucesso!")
        ListaPlayer()
        input("Aperte Enter para retornar...")
        MenuCad()
    elif opcao == "5":  # ---> REMOVER JOGADOR DA LISTA <---
        nt = str
        print("Digite o nome a ser removido da lista de jogadores\n")
        nt = input("Digite o Nome:")
        NomePlayer.remove(nt)
        print("O nome do Jogador ",nt," Foi removida da lista de membros!")
        input("Aperte Enter para retornar...")
        MenuCad()
    elif opcao == "6":  # ---> Retornar ao Menu Principal <---
        print("retornando ao meu principal ~~~")
        sleep(1.3)
        Menuo()
    elif opcao == "7":
        exit()
    else:  # Sempre que não digitar uma opção invalida
        print("Você entendeu as opções? Faça direito!")
        print("Você digitou: ",opcao)
        input("Enter P/ Continuar..")
        MenuCad()  


def Menuo():         # ---> MENU PRINCIPAL <--- Desenho
    os.system("cls") #chama comando do sistema operacional, no caso o comando "cls"
    print("Iniciando treinamento Python\nProjeto controle Moriquendi Federation")
    print("===================================================================")
    print("==                                                               ==")
    print("==                    Moriquendi Federation                      ==")
    print("==                                                               ==")
    print("==  1- Procurar Membro                                           ==")
    print("==  2- Quantidade de Membros                                     ==")
    print("==  3- Fechar                                                    ==")
    print("==                                                               ==")
    print("===================================================================\n")
    print("Opções escolhidas:",contador,"\n")
    Escolha()

