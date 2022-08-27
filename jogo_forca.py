import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
import termcolor
from termcolor import colored
import os
import time

url1 = 'https://www.dicio.com.br/animais-de-a-a-z/'
url2 = 'https://www.dicio.com.br/frutas-de-a-a-z/'
url3 = 'https://www.dicio.com.br/objetos-de-a-a-z/'
url4 = 'https://www.dicio.com.br/paises-de-a-a-z/'


def buscar_informação(url):

    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    texts = soup.find_all('li')
    lista = []
    nova_index = []

    for i in texts:

        lista.append(i.get_text())
    tamanho_lista = len(lista)

    for j in range(0, tamanho_lista):

        palavra = str(lista[j])

        while palavra[0].lower() == 'z':
            nova_index.append(j)
            break

        while palavra[-1] == '.' or palavra[-1] == ';':
            palavra = palavra[:-1]
            lista[j] = palavra
            break
    base_dados = lista[:int(nova_index[-1]) + 1]

    aleatorio = random.choice(base_dados)

    return aleatorio


def bem_vindo():

    cont = 0

    while cont == 0:

        os.system('clear')
        print(colored(' OLÁ, VEM VINDO AO JOGO DA FORCA '.center(50, '*'), 'yellow'))
        for i in range(2):
            print(colored('*******************'.center(50, '*'), 'yellow'))
        print(colored(' ESCOLHA UMA CATEGORIA PARA INICIAR '.center(50, '*'), 'yellow'))
        print(colored('*******************'.center(50, '*'), 'yellow'))
        print(colored(
            '<1> ************************************ (ANIMAIS)'.center(0, '*'), 'yellow'))
        print(colored(
            '<2> ************************************* (FRUTAS)'.center(0, '*'), 'yellow'))
        print(colored(
            '<3> ************************************ (OBJETOS)'.center(0, '*'), 'yellow'))
        print(colored(
            '<4> ************************************* (PAISES)'.center(0, '*'), 'yellow'))
        print(colored('*******************'.center(50, '*'), 'yellow'))

        escolha = int(input('Digite sua resposta: '))
        cont = 1

        if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
            print(colored('RESPOSTA INVALIDA. TENTE NOVAMENTE!'.center(50, '*'), 'red'))
            time.sleep(1)
            cont = 0
        else:
            cont = 1

        if escolha == 1:
            escolha = url1
        elif escolha == 2:
            escolha = url2
        elif escolha == 3:
            escolha = url3
        else:
            escolha = url4

    return escolha


def visual_categoria(categoria, quant_tentativas):

    #resposta = ''

    if categoria == url1:
        resposta = "ANIMAIS"
    elif categoria == url2:
        resposta = "FRUTAS"
    elif categoria == url3:
        resposta = "OBJETOS"
    else:
        resposta = "PAISES"

    os.system('clear')
    print(colored(' VAMOS COMCEÇAR O JOGO '.center(50, '*'), 'yellow'))
    for i in range(2):
        print(colored('*******************'.center(50, '*'), 'yellow'))
    print(
        colored(f' VOCE ESCOLHEU A CATEGORIA {resposta} '.center(50, '*'), 'yellow'))
    print(colored('*******************'.center(50, '*'), 'yellow'))
    for i in range(1):
        print(colored('*******************'.center(50, '*'), 'yellow'))
    print(
        colored(f' VOCE TEM NO TOTAL {quant_tentativas} TENTATIVAS'.center(50, '*'), 'yellow'))
    print(colored('*******************'.center(50, '*'), 'yellow'))


def jogar():

    categoria = bem_vindo()
    palavra = buscar_informação(categoria)
    secreto = palavra

    tamanho = len(palavra)
    vazio = ['_'] * tamanho

   # calculando a quantidade de tentativa por palavra
    for i in range(0, tamanho):

        count = 1

        for j in range(i+1, tamanho):

            if(palavra[i] == palavra[j] and palavra[i] != ' '):
                count = count + 1
                palavra = palavra[:j] + '0' + palavra[j+1:]

    quant_tentativas = (len(palavra) - palavra.count('0'))*2

    visual_categoria(categoria, quant_tentativas)

    # usuario vai chutando letras e o prgama devolve acerto ou erro
    while True and quant_tentativas > 0:

        chute = str(input('Digite uma letra: ')).lower()
        os.system('clear')

        if chute in palavra:
            print(
                f'VOCÊ ACERTOU UM LETRA! {quant_tentativas - 1} TENTATIVAS RESTANDO')
            print('\n')

            for k in range(0, tamanho):
                if chute == palavra[k]:
                    vazio[k] = palavra[k]
            quant_tentativas -= 1

            if quant_tentativas == 0:
                print("PARABENS VOCE ACERTOU A PALAVRA!:)")
            else:
                print(f"VOCE TEM {quant_tentativas} CHANCES")

        else:
            print(
                f'VOCÊ ERROU UM LETRA! {quant_tentativas - 1} TENTATIVAS RESTANDO')
            print('\n')
            quant_tentativas -= 1

        print(vazio)
        print('\n')
    print(f'Palavra secreta: {secreto.upper()}')


def definir_parametros():
    pass


jogar()
