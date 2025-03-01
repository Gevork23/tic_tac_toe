from gameparts import Board

game = Board()
game.display()
game.make_move(1, 1, 'X')
game.make_move(0, 0, 'X')
print('Ход сделан!')
game.display()
