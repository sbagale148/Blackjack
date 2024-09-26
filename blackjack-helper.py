from random import randint

def print_card_name(card_rank):
    card_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    if card_rank in card_names:
        print(f'Drew a {card_names[card_rank]}')
    elif 1 < card_rank < 11:
        print(f'Drew a {card_rank}')
    else:
        print('BAD CARD')

def draw_card():
    num = randint(1, 13)
    print_card_name(num)
    if num == 1:
        return 11
    elif num >= 11:
        return 10
    return num

def print_header(message):
    print('-----------')
    print(message)
    print('-----------')

def draw_starting_hand(name):
    print_header(name.upper() + ' TURN')
    hand_total = draw_card() + draw_card()
    return hand_total

def check_blackjack_or_bust(hand_value, name):
    if hand_value == 21:
        print(f'{name} have BLACKJACK!')
        return True
    elif hand_value > 21:
        print(f'{name} hand is {hand_value}. BUST!')
        return True
    return False

def print_end_turn_status(hand_value):
    print('Final hand: ' + str(hand_value))
    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21:
        print('BUST.')

def print_end_game_status(user_hand, dealer_hand):
    print('-----------')
    print('GAME RESULT')
    print('-----------')
    if user_hand > 21 or user_hand < dealer_hand <= 21:
        print('Dealer wins!')
    elif dealer_hand > 21 or dealer_hand < user_hand <= 21:
        print('You win!')
    else:
        print('Push (tie).')