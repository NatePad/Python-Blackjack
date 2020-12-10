from art import shuffled
import random

deck = []
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♠', '♥', '♦', '♣']



def build_deck():
    deck.clear()

    for suit in suits:
        for i in range(len(faces)):
            card = {}
            card['face'] = faces[i]
            card['suit'] = suit

            if i == 0:
                card['value'] = 1
            elif i < 10:
                card['value'] = int(faces[i])
            else:
                card['value'] = 10

            deck.append(card)

    random.shuffle(deck)
    print(shuffled)



def deal_card(person):
    person['hand'].append(deck.pop())
    person['value'] = get_hand_val(person['hand'])



def deal_hits(player, dealer):
    if player['hit']:
        hs = input('Do you want to "h"it or "s"tay? ').lower()
        while hs not in ['h', 's']:
            print(f'{hs} is not a valid option.')
            hs = input('Do you want to "h"it or "s"tay? ').lower()

        if hs == 's':
            player['hit'] = False
        else:
            deal_card(player)
            print_hand('Your', player)

            if player['value'] > 21:
                print('You went over 21! You bust!')
                player['hit'] = False
    
    if dealer['hit']:
        if dealer['value'] < 17:
            deal_card(dealer)
            print('The dealer hits.')
            print(f"The dealer has {len(dealer['hand'])} cards.")
        else:
            dealer['hit'] = False
            print('The dealer stays.')



def get_hand_val(hand):
    value = 0
    ace_count = 0

    for card in hand:
        if card['value'] == 1:
            ace_count += 1
        else:
            value += card['value']

    if ace_count > 0:
        value += ace_count + 10
        if value > 21:
            value -= 10

    return value



def get_card_string(card):
    return f"{card['face']} of {card['suit']}"



def initial_deal(player, dealer):
    for _ in range(2):
        deal_card(player)
        deal_card(dealer)



def print_hand(name, dict):
    print('_______________')
    if name == 'Your':
        print('Your cards:')
    for card in dict['hand']:
        print(get_card_string(card))
    print(f"Value: {dict['value']}")
    print('***************')
