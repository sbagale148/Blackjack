from blackjack_helper import *

def play_blackjack():
    user_hand = draw_starting_hand('your')
    
    if check_blackjack_or_bust(user_hand, 'Your'):
        return
    
    is_hit = True
    while user_hand < 21 and is_hit:
        hit = input('You have ' + str(user_hand) + '. Hit (y/n)? ').lower()
        if hit == 'n':
            is_hit = False
        elif hit == 'y':
            user_hand += draw_card()
        else:
            print("Invalid input, please enter 'y' or 'n'.")
        if check_blackjack_or_bust(user_hand, 'Your'):
            return

    print_end_turn_status(user_hand)

    # Dealer's turn
    dealer_hand = draw_starting_hand('dealer')
    while dealer_hand < 17:
        print('Dealer has ' + str(dealer_hand) + '.')
        dealer_hand += draw_card()

    print_end_turn_status(dealer_hand)
    print_end_game_status(user_hand, dealer_hand)

    # Ask to replay
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay == 'y':
        play_blackjack()

# Start the game
if __name__ == "__main__":
    play_blackjack()