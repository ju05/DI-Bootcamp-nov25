board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

board[1][2] = 'X'
print(board)

def print_board(board):
    print('*' * 17)
    print(f'*    {board[0][0]}|{board[0][1]}|{board[0][2]}    *')
    print(f'*    {board[0][0]}|{board[0][1]}|{board[0][2]}    *')
    print(f'*    {board[0][0]}|{board[0][1]}|{board[0][2]}    *')


print_board(board)