'''
    Cara ou coroa
    O jogo deve continuar enquanto o usuário quiser jogar.
    Em cada partida, o usuário informa se escolhe cara (0) ou coroa (1)
    e no final de cada uma, é exibida a mensagem se ele ganhou ou perdeu
    Ao término de todas as partidas, deverá ser exibido o totalizador
'''

import random

resultado = {
    'jogador': 0,
    'computador': 0
}

while True:
    escolha = int(input('Cara (0) ou Coroa (1): '))
    numero_aleatorio = random.randint(1, 100)
    # Outra forma de fazer o randômico: round(random.random() * 100)

    if escolha == numero_aleatorio % 2:
        print('Você ganhou !!!')
        resultado['jogador'] += 1
    else:
        print('Voce perdeu.')
        resultado['computador'] += 1

    resposta = input('Deseja jogar novamente (s/n): ')

    if resposta == 'n':
        break

print('\nFim de jogo')
print('Jogador: ' + str(resultado['jogador']))
print('Computador: ' + str(resultado['computador']))