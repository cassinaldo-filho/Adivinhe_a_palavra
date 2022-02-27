import io

from random import randint


def jogar():
    all_words = []

    with open('Lista_palavas.txt', 'r', encoding="utf8") as lista:
        for conteudo in lista:
            all_words.append(conteudo)
    aleatorio = len(all_words)

    word = all_words[randint(0, aleatorio - 1)]

    palavra = ['__', '__', '__', '__', '__', '__', '__', '__']
    errado = []
    for cont in range(0, 6):
        advinhar = input('\n\nChute uma letra...\n')

        errado.append(advinhar)
        errado.append(' ')
        print(f'Você já chutou : ',end='',)
        for x in errado:
            print(f'{x}',end='')
        achou = 0
        for cont2 in range(0, 8):

            if advinhar in word[cont2]:
                palavra[cont2] = advinhar
                achou = 1


        if achou == 1:
            print('\nPalavra misteriosa: ', end='')
            for x in palavra:
                print(f'{x}', end=' ')
        elif achou == 0:
            print(f'\nA palavra não tem a letra "{advinhar}".')
            print('\nPalavra misteriosa: ', end='')
            for x in palavra:
                print(f'{x}', end=' ')


    last_round = input('\n\nDigite qual é a palavra misteriosa.\n') + '\n'

    if last_round == word:
        print(f'Parabens você acertou. A palavra era {word}')
    else:
        print(f'Infelizmente você errou. A palavra era {word}')


while True:

    dec = input('Jogar - 1 //  Sair -2 \n')
    if dec == '1':
        jogar()
    elif dec == '2':
        break
    else:
        print('Valor inválido\n')
