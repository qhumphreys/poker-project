#Creates a card with a suit and value
#Includes a tuple of the names of every card
class Card:
    card_names = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
    def __init__(self, suit:str, value: int):
        self.suit = suit
        self.value = value

    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def __repr__(self):
        return f"{Card.card_names[self.value-2]} of {self.suit}"

    def image_file_name(self):
        return f"Poker/cards/{Card.card_names[self.value-2].lower()}_of_{self.suit.lower()}.png"