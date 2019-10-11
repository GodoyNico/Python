def check_ganhou(board,usado):

    return ((board[1] == usado and board[2] == usado and board[3] == usado) or #vitória horizontal baixo
    (board[4] == usado and board[5] == usado and board[6] == usado) or #vitória horizontal meio
    (board[7] == usado and board [8] == usado and board[9] == usado) or #vitória horizontal alto
    (board[1] == usado and board[4] == usado and board[7] == usado) or #vitória vertical esquerda
    (board[2] == usado and board[5] == usado and board[8] == usado) or #vitória vertical meio
    (board[3] == usado and board[6] == usado and board[9] == usado) or #vitória vertical direita
    (board[1] == usado and board[5] == usado and board[9] == usado) or #vitória diagonal 1
    (board[3] == usado and board[5] == usado and board[7] == usado) or #vitória diagonal 2
