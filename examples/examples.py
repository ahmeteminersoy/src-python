import itertools

players = ['ali', 'veli', 'selami', 'ayşe', 'fatma']

for player1, player2 in itertools.combinations(players, 2):
    print(player1, '<--->', player2)
