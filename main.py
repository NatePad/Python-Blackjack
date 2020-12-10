from art import logo
from os import system, name
import cards

dealer_wins = 0
play_again = True
player_wins = 0
ties = 0


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def print_score():
    print('_______________')
    print(f'Player Wins: {player_wins}')
    print(f'Dealer Wins: {dealer_wins}')
    print(f'Ties: {ties}')
    print('***************')


while play_again:
    player = {
        'hand': [],
        'hit': True,
        'value': 0
    }
    dealer = {
        'hand': [],
        'hit': True,
        'value': 0
    }

    clear()
    print(logo)

    if len(cards.deck) < 26:
        cards.build_deck()
    
    # INITIAL DEAL
    cards.initial_deal(player, dealer)

    # REVEAL THE DEALER'S FIRST CARD
    print(f"The dealer has the {cards.get_card_string(dealer['hand'][0])}.")

    # SHOW THE PLAYER'S CARDS
    cards.print_hand('Your', player)

    # DEAL HITS
    while player['hit'] or dealer['hit']:
        cards.deal_hits(player, dealer)


    # REVEAL THE DEALER'S CARDS
    print("_______________")
    print("DEALER'S CARDS:")
    cards.print_hand("Dealer's", dealer)


    # DETERMINE WINNER
    if player['value'] > 21:
        if dealer['value'] > 21:
            ties += 1
            print("You both bust! It's a draw!")
        else:
            dealer_wins += 1
            print('You bust. The dealer wins.')
    elif dealer['value'] > 21:
        player_wins += 1
        print('The dealer bust! You win!')
    elif player['value'] > dealer['value']:
        player_wins += 1
        print('You win!')
    elif player['value'] < dealer['value']:
        dealer_wins += 1
        print('The dealer wins.')
    else:
        if player['value'] != 21 or (len(player['hand']) > 2 and len(dealer['hand']) > 2):
            ties += 1
            print("It's a tie!")
        else:
            if len(player['hand']) == 2:
                if len(dealer['hand']) == 2:
                    ties += 1
                    print("You both got Blackjack! It's a draw!")
                else:
                    player_wins += 1
                    print('You break the tie with a Blackjack! Congratulations!')
            else:
                dealer_wins += 1
                print('The dealer breaks the tie with a Blackjack!')


    print_score()


    yn = input('Do you want to play again? y/n: ').lower()
    while yn not in ['y', 'n']:
        print(f'{yn} is not a valid option.')
        yn = input('Do you want to play again? y/n: ').lower()

    if yn == 'n':
        play_again = False
