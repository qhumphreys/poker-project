#Creates a deck with 52 cards
#Contains a method to shuffle the deck and deal the top card
#Contains two tuples and the append, extend, and pop methods
from Card import Card
import random
class Deck:
    suits = ("hearts", "diamonds", "spades", "clubs")
    values = (2,3,4,5,6,7,8,9,10,11,12,13,14)
   
    def __init__(self):
        self.all_cards = []
        for suit in Deck.suits:
            cards_in_suit = []
            for value in Deck.values:
                cards_in_suit.append(Card(suit = suit, value = value))
            self.all_cards.extend(cards_in_suit)

    def get_deck(self):
        return self.all_cards
    
    def print_deck(self):
        for card in self.all_cards:
            print(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        dealt_card = self.all_cards[0]
        self.all_cards.pop(0)
        return dealt_card