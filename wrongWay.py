values = ('2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A') # cartas
suits = ('h', 'c', 'd', 's') #naipes

class Card:
    def __init__(self, value, suit):
        self.value, self.suit = value, suit

if __name__ == '__main__':
    card1 = Card('J', 'h')
    card2 = Card('J', 'h')
    print ("Card 1: %s" % id(card1))
    print ("Card 2: %s" % id(card2))
