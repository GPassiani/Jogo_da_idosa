print('jogo da idosa')
#Projeto jogo da idosa
tabuleiro = [
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i']
             ]

vez_jogador = "X"

jogadas = 0
def apresentatabuleiro():
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])
    
def verificavencedor():
    for linha in range(3):
        if tabuleiro [linha][0] == \
            tabuleiro[linha][1] == \
            tabuleiro[linha][2]:
            print('Vencedor')
            return True
    for coluna in range(3):
        if tabuleiro[0][coluna] == \
            tabuleiro[1][coluna] ==\
            tabuleiro [2][coluna]:
            print("Vencedor coluna")
            return True
    if tabuleiro [0][0] == tabuleiro [1][1] == tabuleiro[2][2] or \
        tabuleiro[2][0] == tabuleiro [1][1] == tabuleiro [0][2]:
        print("Vencedor")
        return True
    return False
while jogadas < 9:
    print(f'Rodada {jogadas}')
    apresentatabuleiro()
    posicao = input(f'{vez_jogador} Insira qual posição preencher:')

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == posicao:
                tabuleiro[linha][coluna] = vez_jogador
                jogada_realizada = True
                
                
    if verificavencedor():
        continuar_jogo = input("")
        print(f'Vencedor foi o jogador {vez_jogador}')    
        break       
    
    if jogada_realizada == True:
        vez_jogador = "O" if vez_jogador == "X" else "X"
        jogadas += 1
        
    
    
    
      