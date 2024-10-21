#Shuffles the deck, inserts 4 hands to a poker game, and deals 5 cards to each hand
#Uses the compare method in a tournament style to find the winner
#Creates a row for each hand, and concatenates them into a grid
#Creates text based on the rank of each hand, and prints the winner
from Deck import Deck
from Card import Card
from Hand import Hand
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_row(img1, img2, img3, img4, img5):
    row = Image.new(mode="RGB", size=(img1.width*5,img1.height))
    row.paste(img1, (0, 0))
    row.paste(img2, (img1.width, 0))
    row.paste(img3, (img1.width*2, 0))
    row.paste(img4, (img1.width*3, 0))
    row.paste(img5, (img1.width*4, 0))
    return row

def create_grid(row1,row2,row3,row4):
     bg = Image.new(mode="RGB", size=(625,580))
     bg.paste(row1, (0,0))
     bg.paste(row2, (0, row1.height))
     bg.paste(row3, (0, row1.height*2))
     bg.paste(row4, (0, row1.height*3))
     return bg

class Main:
    deck = Deck()
    poker_game = []
    deck.shuffle()
    hand = Hand()
    hand2 = Hand()
    hand3 = Hand()
    hand4 = Hand()
    poker_game.insert(0, hand)
    poker_game.insert(1, hand2)
    poker_game.insert(2, hand3)
    poker_game.insert(3, hand4)

    for x in range(5):
        hand.add_card(deck.deal_card())
        hand2.add_card(deck.deal_card())
        hand3.add_card(deck.deal_card())
        hand4.add_card(deck.deal_card())

    is_tie1 = False
    is_tie2 = False
    winner = hand
    if hand.compare(hand2) == 1:
        winner1 = hand
        winner_name = "hand1"
    elif hand.compare(hand2) == -1:
        winner1 = hand2
        winner_name = "hand2"
    else:
        is_tie1 = True
        
    if hand3.compare(hand4) == 1:
        winner2 = hand3
        winner_name = "hand3"
    elif hand3.compare(hand4) == -1:
        winner2 = hand4
        winner_name = "hand4"
    else:
        is_tie2 = True
    
    if is_tie1 == False and is_tie2 == False:
        if winner1.compare(winner2) == 1:
            winner = winner1
        elif winner1.compare(winner2) == -1:
            winner = winner2

    if is_tie1 == False and is_tie2 == True:
        winner = winner1
        

    if is_tie1 == True and is_tie2 == False:
        winner = winner2


    row1 = create_row(
            Image.open(hand.hand[0].image_file_name()),
            Image.open(hand.hand[1].image_file_name()),
            Image.open(hand.hand[2].image_file_name()),
            Image.open(hand.hand[3].image_file_name()),
            Image.open(hand.hand[4].image_file_name())
            )
    row2 = create_row(
            Image.open(hand2.hand[0].image_file_name()),
            Image.open(hand2.hand[1].image_file_name()),
            Image.open(hand2.hand[2].image_file_name()),
            Image.open(hand2.hand[3].image_file_name()),
            Image.open(hand2.hand[4].image_file_name())
            )
    row3 = create_row(
            Image.open(hand3.hand[0].image_file_name()),
            Image.open(hand3.hand[1].image_file_name()),
            Image.open(hand3.hand[2].image_file_name()),
            Image.open(hand3.hand[3].image_file_name()),
            Image.open(hand3.hand[4].image_file_name())
            )
    row4 = create_row(
            Image.open(hand4.hand[0].image_file_name()),
            Image.open(hand4.hand[1].image_file_name()),
            Image.open(hand4.hand[2].image_file_name()),
            Image.open(hand4.hand[3].image_file_name()),
            Image.open(hand4.hand[4].image_file_name())
            )
    grid = create_grid(row1,row2,row3,row4)

    draw = ImageDraw.Draw(grid)
    font = ImageFont.truetype('Arial', 15)
    win_font = ImageFont.truetype('Arial', 25)

    if winner == hand:
        draw.text((grid.width-115,25), "WINNER!", font = win_font, fill=(255,0,0))
    elif winner == hand2:
        draw.text((grid.width-115,185), "WINNER!", font = win_font, fill=(255,0,0))
    elif winner == hand3:
        draw.text((grid.width-115,300), "WINNER!", font = win_font, fill=(255,0,0))
    else:
        draw.text((grid.width-115,460), "WINNER!", font = win_font, fill=(255,0,0))

  
    draw.text((515,70), hand.get_hand_type(), font=font, fill = (255,255,255))
    draw.text((515,220), hand2.get_hand_type(), font=font, fill = (255,255,255))
    draw.text((515,355), hand3.get_hand_type(), font=font, fill = (255,255,255))
    draw.text((515,510), hand4.get_hand_type(), font=font, fill = (255,255,255))
    
    grid.show()
    # print(hand.get_hand_type())
    # print(hand2.get_hand_type())
    # print(hand3.get_hand_type())
    # print(hand4.get_hand_type())
    # print(winner_name)