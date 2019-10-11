import random
def escolha_primeiro():
    if random.randint(1,2) == 1:
        return 'Jogador 1'
    else:
        return 'Jogador 2'
