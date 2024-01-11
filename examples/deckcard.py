import random
card_values = {"As": 14, "Papaz": 13, "Kız": 12, "Vale": 11, "10": 10,
               "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
card_types = {"Maça": 3,"Sinek": 2,"Karo": 1,"Kupa": 0}

def build_deck():
    deck = []
    for cval in card_values:
        for ctype in card_types:
            deck.append((cval, ctype))
    return deck
def distribute(deck):
    random.shuffle(deck)
    players = [[], [], [], []]

    for i in range(52):
        players[i % 4].append(deck[i])
    for player in players:
        player.sort(key= keyfunc, reverse=True)
    return players

def keyfunc(t):
    cval, ctype = t
    return card_values[cval] * 4 + card_types[ctype]
def disp_players(players):  
    for player in players:

        print(player)
        print('-------')
  
def main():
    deck = build_deck()
    players = distribute(deck)
    disp_players(players)
    
main()  