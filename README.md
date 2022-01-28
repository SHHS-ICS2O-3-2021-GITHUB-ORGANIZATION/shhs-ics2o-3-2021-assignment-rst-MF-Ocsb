# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM: Blackjack Blizzard
# DATE OF CREATION: 28/01/22
# PURPOSE OF PROGRAM: Play Blackjack with a Yeti

# VARIABLE DEFINITION
foo = 0
score = 100
bet = 0
card = 0
card_Count = 0
yeti_Card = 0
yeti_Count = 0
ace = 11
mode = 0
yeti_Agg = 0
# String variables to be printed in settings
scoreString = str(score)
aceString = str(ace)
yeti_AggStr = str(yeti_Agg)
# Import random for use in dealing
import random
from random  import randint

while True:

  while mode == 0:
    # Mode for easy user navigation
    mode = int(input("\nWelcome to Blackjack Blizzard!\n1 - Play\n2 - Settings\n3 - Rules\n4 - Quit\n"))

  while mode == 2:
    # Let User set the Ace and Yeti values

    print(("\nAce value = ") + aceString)
    foo = int(input("Ace value (1 or 11): "))

    # Only 11 and 1 are used in blackjack so only those options will be allowed.

    if foo == 1:
      ace = 1
    elif foo == 11:
      ace = 11
    else:
      ace = 11
    aceString = str(ace)
    
    print(("Yeti Aggression = ") + yeti_AggStr)
    yeti_Agg = int(input("Yeti Aggression: "))
    yeti_AggStr = str(yeti_Agg)
    mode = 0
  
  while mode == 3:
    # Show rules for players who don't know
    print("Blackjack is the same kind of game as 21. You draw cards until you decide to stand, while being as close as possible to 21, without going over. Then, you and your opponent show your score, and whoever is closer to 21 wins. You can bet chips to get more chips, with the goal of getting the highest score possible.\n\nDo not worry about the Yeti. He doesn't affect the game. His name is Clifford.")
    input("Press enter when you understand.")
    mode = 0

  if mode == 4:
    quit("Play again sometime!")
  
  while mode == 1:
    # Allow the user to choose between bets or no bets
    foo = input("\n1 - Scored\n2 - Free Play\n3 - Back\n")
    if foo == 1:
      mode = 5
    elif foo == 2:
      mode = 6
    else:
      mode = 0

  while mode == 5:
    # The user can't bet more than they have. After they bet, remove that amount.
    print(("Current score: ") + bet)
    bet = int(input("Place your bet: "))
    if bet > score:
      bet = score
    scoreString = str(score)
    score = score - bet

  print("The Yeti deals the first two cards.")
  card = randint(1,10)

