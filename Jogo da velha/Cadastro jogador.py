def cadastro_jogador():

    marcador = ''
    while not (marcador == 'X' or marcador == 'O'):
        marcador = input('Jogador 1, você quer ser X ou O? ').upper()

        if marcador == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
