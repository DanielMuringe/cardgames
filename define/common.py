#Imports
## Bultin modules
from random import choice as rand_choice


colours = ['black','red']
ranks   = ['a','j']+list(range(2,11))+['k','q','joker']
suites  = ['ace','clover','diamond','heart','joker']

'''
The name <card> refers to the index of the card in all scopes.
'''


# Define Card class
class Card():
    '''
    Attributes(all are integer types):
        rank
        suite
        colour
    '''

    def __init__(self,card_no:int):
        self.card_no    = card_no
        self.rank:int   = 13 if self.card_no>51 else self.card_no%13
        self.suite:int  = 4 if self.card_no>51 else int(self.card_no/13)
        self.colour:int = abs(52-self.card_no) if self.card_no>51 else int(self.suite/2)

    def __str__(self):
        return f'{ranks[self.rank]} {suites[self.suite]} {colours[self.colour]}'


#Define Player class
class Player():
    def __init__(self):
        self.held_cards:list    = []
        self.dropped_cards:list = []
        self.needed:int         = 0

    def drop(self,dropped_card):
        self.dropped_cards.append(dropped_card)
        self.held_cards.remove(dropped_card)
    
    def pick(self,given_card):
        self.held_cards.append(given_card)


#Define Dealer class 
class Dealer():
    '''
    The class enables a player interact with the deck and rules with of the game
    '''
    def __init__(self,players,min_cards=3,max_cards=8,min_players=2,max_players=8):
        self.players     = players
        self.deck        = list(range(54))
        self.min_cards   = min_cards
        self.max_cards   = max_cards
        self.min_players = min_players
        self.max_players = max_players

    def shuffle(self):
        _deck         = self.deck
        shuffled_deck = []
        for card in self.deck:
            selected_card = rand_choice(_deck)
            shuffled_deck.append(selected_card)
            _deck.remove(selected_card)
        self.deck = shuffled_deck

    def give(self,player):
        for x in range(player.needed_cards):
            given_card = rand_choice(self.deck)
            player.pick.append(given_card)
            self.deck.remove(given_card)
        player.needed_cards = 0

    def distribute(self):
        self.shuffle()
        for player in self.players:
            player.needed_cards = self.min_cards
            self.give(player)
    
    def game_over(self,assess_func,winner):
        self.winner = winner
        return assess_func()
