from replit import clear
import random as r
from art import logo
import time as t

deck = [  11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
          11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
          11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
          11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
          
cards = []
game = True


def boot():
    """
  Prints logo art and welcome message.  
  """
    print(logo)
    print("Welcome to The Royal Blackjack Casino\n")

def setup(players):
    """
  Start the game by dealing the starting cards to the players hand
  """
    boot()
    global cards
    cards = deck.copy()
    # print(cards)
    num_players = int(input("How many players are there?\n"))
    for player in range(num_players):
        key = "Player_" + str(player + 1)
        players[key] = [deal_card(), deal_card()]
    return players, num_players

def deal_card():
  """this function deals a single card to the hand"""
  deal =  r.choice(cards)
  cards.pop(deal)
  return deal

def players_choice(players, num_players):
    """Allows players to see their hand decide if they would like to add another card to their hand."""
    for player in range(num_players):
        key = "Player_" + str(player + 1)
        print(
            f"{key} hand is {players[key]} with a sum of {has_ace(players[key])}")
        choice = (input("Do you want to draw another card? 'y' or 'n'\n"))
        while choice != 'n':
            if choice == 'y':
                players[key].append(deal_card())
            else:
                print("Invalid choice, choose again.")
            print(
                f"{key} hand is {players[key]} with a sum of {has_ace(players[key])}"
            )
            choice = (input("Do you want to draw another card? 'y' or 'n'\n"))
        clear()
    return players

def dealer_move(hand):
    """Dealer's move"""
    print("Please wait while the Dealer makes a move")   
    
    if has_ace(hand) > 15:
        return hand
    else:
        while has_ace(hand) <= 15:
            hand.append(deal_card())
        return hand

def is_black_jack(hand):
    """Check if the hand is a Black Jack"""
    if sum(hand) == 21:
      return True
    else:
      return False

def win_or_lose(hand):
    # Check if hand is more than 21
    # True => lose
    # False = > in the game

    if sum(hand) > 21:
        if '11' in hand:
            ace_hand = sum(hand) - 10
            # Checks if ace hand is more than 21
            if ace_hand > 21:
                return True
            else:
                return False
        else:
            return True
    return False

def has_ace(hand):
  value = sum(hand)
  if 11 in hand and value > 21:
    return value - 10
  else:
    return value

def compare(players, num_players):
  """Compare the hands of the dealer and players"""
  
  # Win or Lose Flag Dictionary
  win_lose = players.copy()
  # print(win_lose)

  for player in players:
    # Check if black jack
    if is_black_jack(players[player]):
      win_lose[player] = "BlackJack"
    else:
      win_lose[player] = win_or_lose(players[player])
  
  # print(f"{win_lose} ====> Win / Lose")
  # print(f"{players} ====> Players")

  # If Dealer did not get BJ or > 21. Evaluate players hand
  if win_lose["Dealer"] == False:
    # Compute winners. Players with smaller cards lose
    for player in range(num_players):
        key = "Player_" + str(player + 1)
        if  win_lose[key] == False and has_ace(players["Dealer"]) > has_ace(players[key]):
          win_lose[key] = True
  
  return win_lose

def winners(prelim, players, num_players):
    if prelim["Dealer"] == 'BlackJack':
      print("Dealer got a BlackJack!")
      for player in range(num_players):
        key = "Player_" + str(player + 1)
        if prelim[key] == True or prelim[key] == False:
          print(f"{[key]}'s hand: {has_ace(players[key])} loss to the Dealer")
        else:
          print(f"{[key]}'s hand: {has_ace(players[key])} won nothing")
    elif prelim["Dealer"] != 'BlackJack':
      for player in range(num_players):
        key = "Player_" + str(player + 1)
        if prelim[key] != True:
          if prelim[key] =='BlackJack' or has_ace(players['Dealer']) > has_ace(players['Dealer']) :
            print(f"{[key]}'s hand: {has_ace(players[key])} beat the Dealer's hand: {has_ace(players['Dealer'])}")
          else:
            print(f"{[key]}'s hand: {has_ace(players[key])} loss to the Dealer's hand: {has_ace(players['Dealer'])}")
        else:
          print(f"{[key]}'s hand: {has_ace(players[key])} loss to the Dealer's hand: {has_ace(players['Dealer'])}")

while game:
    # Initialise Variables
    players = {"Dealer": []}

    # How many players are there?
    # num_players = int(input("How many players are there?\n"))
    players, num_players = setup(players)

    # Dealer deals
    players["Dealer"] = [deal_card(), deal_card()]
    # print(players)

    # Players Choice
    clear()
    players = players_choice(players, num_players)

    # Dealer Makes Choice

    # print("Please wait while the Dealer makes a move")
    players["Dealer"] = dealer_move(players["Dealer"])
    print(
        f"Dealer's hand is {players['Dealer']} with a sum of {has_ace(players['Dealer'])}"
    )
    t.sleep(2)
    clear() 
    # Tabulate scores
    prelim = compare(players, num_players)
    # print(prelim)
    winners(prelim, players,num_players)
    t.sleep(3)   
    # print(cards)
    restart = ''
    while restart != 'y' or restart != 'n':
      restart = input("Would you like to play again? 'y' or 'n'\n")
      if restart == 'y':
        clear()
        break
      else:
        game = False
        print("Thanks for playing! ~ creator: Andy Ye")
        break

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
