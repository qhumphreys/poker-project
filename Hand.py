#Creates a hand with 5 cards, sorts them by value, and reverses it
#Uses method decomposition to determine the rank of a hand. In each mini-method, I analyzed values and suits to find matches
#Also decomposes a compare method to find the winner between two hands. In the mini-methods, I 
#The index method is used in is_royal_flush
from Deck import Deck
from Card import Card
dealt_cards = []
class Hand:
    def __init__(self):
        self.hand = []

    def print_hand(self):
        for card in self.hand:
            print(card)

    def add_card(self, card: Card):
        self.hand.append(card)
        self.hand.sort(key = Card.get_value)
        self.hand.reverse()

    
    def is_pair(self):
        num_pairs = 0
        for x in range(len(self.hand)-1):
            if self.hand[x].get_value() == self.hand[x+1].get_value():
                num_pairs += 1
        return num_pairs == 1
    
    def is_two_pair(self):
        num_pairs = 0
        start_index = 0
        for y in range(2):
            for x in range(start_index, len(self.hand)-1):
                if (self.hand[x].get_value() == self.hand[x+1].get_value() and
                    ((len(self.hand)-1) - start_index ) >= 1
                ):
                        num_pairs += 1
                        start_index = x+2
                        break
        return num_pairs == 2
    
    def is_three_of_kind(self):
        if self.is_two_pair():
            return False
        count = 0
        for x in range(len(self.hand)-1):
            if self.hand[x].get_value() == self.hand[x+1].get_value():
                count += 1
            if count == 2:
                return True
        return False

    def is_four_of_kind(self):
        if self.is_full_house():
            return False
        count = 0
        for x in range(len(self.hand)-1):
            if self.hand[x].get_value() == self.hand[x+1].get_value():
                count += 1
        return count == 3

    def is_straight(self):
        values = []
        for x in self.hand:
            values.append(x.get_value())
        return values == list(range(max(values), min(values)-1, -1))
    
    def is_flush(self):
       first = self.hand[0].get_suit()
       result = False
       for x in self.hand:
            if x.get_suit() == first:
               result = True
            else:
               return False
       return result
    
    def is_straight_flush(self):
        if self.is_straight() and self.is_flush():
            return True
        else:
            return False
    
    def is_full_house(self):
        if (
            (self.hand[0].get_value() == self.hand[1].get_value() and
            self.hand[2].get_value() == self.hand[3].get_value() and
            self.hand[3].get_value() == self.hand[4].get_value()) or
            (self.hand[0].get_value() == self.hand[1].get_value() and
            self.hand[1].get_value() == self.hand[2].get_value() and
            self.hand[3].get_value() == self.hand[4].get_value())
            ):
            return True
        else:
            return False
    
    def is_royal_flush(self):
        values = []
        for x in self.hand:
            values.append(x.get_value())
        if (
            self.is_straight() and
            self.is_flush() and
            values.index(14)==0
            ):
            return True
        else:
            return False
        
    def rank(self):
            if self.is_royal_flush():
                return 9
            elif self.is_straight_flush():
                return 8
            elif self.is_four_of_kind():
                return 7
            elif self.is_full_house():
                return 6
            elif self.is_flush():
                return 5
            elif self.is_straight():
                return 4
            elif self.is_three_of_kind():
                return 3
            elif self.is_two_pair():
                return 2
            elif self.is_pair():
                return 1
            else:
                return 0

    def get_hand_type(self):
            if self.rank() == 0:
                return "High Card"
            if self.rank() == 1:
                return "One Pair"
            if self.rank() == 2:
                return "Two Pair"
            if self.rank() == 3:
                return "Three Of A Kind"
            if self.rank() == 4:
                return "Straight"
            if self.rank() == 5:
                return "Flush"
            if self.rank() == 6:
                return "Full House"
            if self.rank() == 7:
                return "Four Of A Kind"
            if self.rank() == 8:
                return "Straight Flush"
            if self.rank() == 9:
                return "Royal FLush"
            
    def compare(self, other):
        if self.rank() > other.rank():
            return 1
        elif self.rank() < other.rank():
            return -1
        elif self.rank() == 9 and other.rank() == 9:
            return 0
        elif self.rank() == 8 and other.rank() == 8:
            return self.both_straight_flush(other)
        elif self.rank() == 7 and other.rank() == 7:
            return self.both_four_kind(other)
        elif self.rank() == 6 and other.rank() == 6:
            return self.both_full_house(other)
        elif self.rank() == 5 and other.rank() == 5:
            return self.both_flush(other)
        elif self.rank() == 4 and other.rank() == 4:
            return self.both_straight(other)
        elif self.rank() == 3 and other.rank() == 3:
            return self.both_three_kind(other)
        elif self.rank() == 2 and other.rank() == 2:
            return self.both_two_pair(other)
        elif self.rank() == 1 and other.rank() == 1:
            return self.both_pair(other)
        elif self.rank() == 0 and other.rank() == 0:
            return self.both_high_card(other)
        
    def both_straight_flush(self, other_hand):
        #Both straight flushes
        if self.hand[0].get_value() > other_hand.hand[0].get_value():
            return 1
        elif self.hand[0].get_value() < other_hand.hand[0].get_value():
            return -1
        else:
            return 0
            
    def both_flush(self, other_hand):
        #Both flushes    
        if self.hand[0].get_value() > other_hand.hand[0].get_value():
            return 1
        elif self.hand[0].get_value() < other_hand.hand[0].get_value():
            return -1
        else:
            return 0
            
    def both_straight(self, other_hand):
        #Both Straights    
        if self.hand[0].get_value() > other_hand.hand[0].get_value():
            return 1
        elif self.hand[0].get_value() < other_hand.hand[0].get_value():
            return -1
        else:
            return 0
            
    def both_four_kind(self, other_hand):
        #Both Four of a Kind
        if self.hand[2].get_value() > other_hand.hand[2].get_value():
            return 1
        elif self.hand[2].get_value() < other_hand.hand[2].get_value():
            return -1
        else:
            return 0
            
    def both_full_house(self, other_hand):
        #Both Full House
        if self.hand[3].get_value() > other_hand.hand[3].get_value():
            return 1
        elif self.hand[3].get_value() < other_hand.hand[3].get_value():
            return -1
        else:
            return 0
            
    def both_three_kind(self, other_hand):
        #Both Three of a Kind
        if self.hand[3].get_value() > other_hand.hand[3].get_value():
            return 1
        elif self.hand[3].get_value() < other_hand.hand[3].get_value():
            return -1
        else:
            return 0
        
    def both_two_pair(self, other_hand):
        #Both two pair
        if self.hand[0].get_value()==self.hand[1].get_value():
            highest_pair = self.hand[0].get_value()
            if self.hand[2].get_value()==self.hand[3].get_value():
                second_pair = self.hand[2].get_value()
                highest_single = self.hand[4].get_value()
            else:
                second_pair = self.hand[4].get_value()
                highest_single = self.hand[3].get_value()
        else:
            highest_single = self.hand[0].get_value()
            highest_pair = self.hand[2].get_value()
            second_pair = self.hand[4].get_value()

        if other_hand.hand[0].get_value()==other_hand.hand[1].get_value():
            highest_pair2 = other_hand.hand[0].get_value()
            if other_hand.hand[2].get_value()==other_hand.hand[3].get_value():
                second_pair2 = other_hand.hand[2].get_value()
                highest_single2 = other_hand.hand[4].get_value()
            else:
                second_pair2 = other_hand.hand[4].get_value()
                highest_single2 = other_hand.hand[3].get_value()
        else:
            highest_single2 = other_hand.hand[0].get_value()
            highest_pair2 = other_hand.hand[2].get_value()
            second_pair2 = other_hand.hand[4].get_value()
            
        if highest_pair > highest_pair2:
            return 1
        elif second_pair > second_pair2:
            return 1
        elif highest_single > highest_single2:
            return 1
        elif highest_pair < highest_pair2:
            return -1
        elif second_pair < second_pair2:
            return -1
        elif highest_single < highest_single2:
            return -1
        else:
            return 0
    
    def both_pair(self, other_hand):
        if self.rank() == 1 and other_hand.rank() == 1:
            if self.hand[0].get_value() == self.hand[1].get_value():
                high_pair = self.hand[0]
                high_single = self.hand[2]
            else:
                high_single = self.hand[0]
                if self.hand[1].get_value() == self.hand[2].get_value():
                    high_pair = self.hand[2]
                elif self.hand[2].get_value() == self.hand[3].get_value():
                    high_pair = self.hand[3]
                else:
                    high_pair = self.hand[4]

        
            if other_hand.hand[0].get_value() == other_hand.hand[1].get_value():
                high_pair2 = other_hand.hand[0]
                high_single2 = other_hand.hand[2]
            else:
                high_single2 = other_hand.hand[0]
                if other_hand.hand[1].get_value() == other_hand.hand[2].get_value():
                    high_pair2 = other_hand.hand[2]
                elif other_hand.hand[2].get_value() == other_hand.hand[3].get_value():
                    high_pair2 = other_hand.hand[3]
                else:
                    high_pair2 = other_hand.hand[4]


            if high_pair.get_value() > high_pair2.get_value():
                return 1
            elif high_pair.get_value() < high_pair2.get_value():
                return -1
            else:
                if high_single.get_value() > high_single2.get_value():
                    return 1
                elif high_single.get_value() < high_single2.get_value():
                    return -1
                else:
                    return 0

    def both_high_card(self, other_hand):
        if self.hand[0].get_value() > other_hand.hand[0].get_value():
            return 1
        elif self.hand[0].get_value() < other_hand.hand[0].get_value():
            return -1
        else:
            if self.hand[1].get_value() > other_hand.hand[1].get_value():
                return 1
            elif self.hand[1].get_value() < other_hand.hand[1].get_value():
                return -1
            else:
                if self.hand[1].get_value() > other_hand.hand[1].get_value():
                    return 1
                elif self.hand[1].get_value() < other_hand.hand[1].get_value():
                    return -1
                else:
                    if self.hand[2].get_value() > other_hand.hand[2].get_value():
                        return 1
                    elif self.hand[2].get_value() < other_hand.hand[2].get_value():
                        return -1
                    else:
                        if self.hand[3].get_value() > other_hand.hand[3].get_value():
                            return 1
                        elif self.hand[3].get_value() < other_hand.hand[3].get_value():
                            return -1
                        else:
                            if self.hand[4].get_value() > other_hand.hand[4].get_value():
                                return 1
                            elif self.hand[4].get_value() < other_hand.hand[4].get_value():
                                return -1