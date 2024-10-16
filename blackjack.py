# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# USER'S TURN
def blackjack(name):
  user_hand = draw_starting_hand(name.upper() + "'S")
  should_hit = 'y'
  while user_hand < 21:
    should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
    if should_hit == 'n':
      break
    elif should_hit != 'y':
      print("Sorry I didn't get that.")
    else:
      user_hand = user_hand + draw_card()
  print_end_turn_status(user_hand)
  return user_hand

players_num = int(input("Welcome to Blackjack! How many players? "))
players = []
for i in range(1, players_num + 1):
  name = input("What is player " + str(i) + "'s name? ")
  players.append(name)
scores = [3] * players_num
hand_values = [0] * players_num
hand = True
while hand:
  if not players:
    hand = False
  else:
    for i in range(len(players)):
      hand_values[i] = blackjack(players[i])

    # DEALER'S TURN
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
      print("Dealer has {}.".format(dealer_hand))
      dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)

    # GAME RESULT
    print_header('GAME RESULT')
    for i in range(len(hand_values)):
      if print_end_game_status(hand_values[i], dealer_hand) == "L":
        scores[i] = scores[i] - 1
        print(players[i] + " loses! Score: " + str(scores[i]))
        if scores[i] == 0:
          print(players[i] + " eliminated!")
      elif print_end_game_status(hand_values[i], dealer_hand) == "W":
        scores[i] = scores[i] + 1
        print(players[i] + " wins! Score: " + str(scores[i]))
      else:
        print(players[i] + " pushes. Score: " + str(scores[i]))
    new_players = []
    new_hand_values = []
    new_scores = []
    for i in range(len(scores)):
      if scores[i] != 0:
        new_players.append(players[i])
        new_hand_values.append(hand_values[i])
        new_scores.append(scores[i])
    players = new_players
    scores = new_scores
    hand_values = new_hand_values
    if scores:
      play_again = input("Do you want to play another hand (y/n)? ")
      invalid = True
      while invalid:
        if play_again == "n":
          hand = False
          invalid = False
        if play_again == "y":
          invalid = False
    else:
      print("All players eliminated!")