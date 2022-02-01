# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM: Blackjack Blizzard
# DATE OF CREATION: 28/01/22
# PURPOSE OF PROGRAM: 21 with a Yeti

# VARIABLE DEFINITION
# foo is a placeholder variable to fit in with questions that the computer does not need to remember.
temp = 1
score = 100
bet = 0
card = 0
card_Count = 0
yeti_Count = 0
ace = 11
mode = 0
yeti_Agg = 0
tries = 0
wins = 0
# String variables to be printed
scoreString = str(score)
aceString = str(ace)
yeti_AggStr = str(yeti_Agg)
cardString = str(card)
yeti_CountStr = str(yeti_Count)
countString = str(card_Count)
cardString = str(card)
# Import random for use in dealing
import random
from random  import randint

# exit = 0
# while exit != 1

while True:

  while mode == 0:
    # Mode for easy user navigation
    mode = int(input("\nWelcome to Blackjack Blizzard!\n1 - Play\n2 - Settings\n3 - Rules\n4 - Score\n5 - Quit\n"))

  if mode == 4:
    print(("\nYour score is ") + scoreString)
    mode = 0

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
    
    temp = input()
    if temp == "secret password":
      print(("Yeti Aggression = ") + yeti_AggStr)
      yeti_Agg = int(input("Yeti Aggression: "))
      yeti_AggStr = str(yeti_Agg)
    mode = 0
  
  while mode == 3:
    # Show rules for players who don't know
    print("Blackjack is the same kind of game as 21. You draw or (Hit) cards until you decide to stand, while being as close as possible to 21, without going over. Then, you and your opponent show your score, and whoever is closer to 21 wins. You can bet chips to get more chips, with the goal of getting the highest score possible.\n\nDo not worry about the Yeti. He doesn't affect the game. His name is Clifford.")
    input("Press enter when you understand.")
    mode = 0

  if mode == 5:
    quit("Play again sometime!")

  while mode == 1:

      # The loop lets the player do best out of three rounds, and restart at a win or loss anytime.
      while tries < 3 and wins < 2:
        # The user can't bet more than they have.
        card = 0
        card_Count = 0
        yeti_Count = 0
        print(("\nCurrent score: ") + scoreString)
        bet = int(input("Place your bet: "))
        if bet > score:
          bet = score
        scoreString = str(score)
    
        print("\nThe Yeti deals the first two cards.")
        # Change the randint range depending on what they set the ace to
        if ace == 1:
          card = randint(1,10)
          card = randint(1,10) + card
          yeti_Count = yeti_Count + randint(1,10)
          yeti_Count = yeti_Count + randint(1,10)
        elif ace == 11:
          card = randint(2,11)
          card = randint(2,11) + card
          yeti_Count = yeti_Count + randint(2,11)
          yeti_Count = yeti_Count + randint(2,11)

        card_Count = card
        countString = str(card_Count)
        #If they get a 21 on their first turn, they get a blackjack, if they ever cross 21 they bust. The Tries variable lets them restart as soon as they win, for 3 times.
        if card_Count == 21:
          print("Blackjack!")
          temp = 2
        if card_Count > 21:
          print("Bust!")
          temp = 2
        if yeti_Count == 21:
          print("The Yeti got a Blackjack!")
        if yeti_Count > 21:
          print("The Yeti busted!")

        print(("Your card count is: ") + countString)
        temp = int(input("\n1 - Hit\n2 - Stand\n"))

        if ace == 1:
          if temp == 1:  
            print("\nThe Yeti deals you another card.")
            card = randint(1,10)
            print(card)
          if yeti_Count < 16:
            print("\nThe Yeti draws another card.")
            yeti_Count = yeti_Count + randint(1,10)
        elif ace == 11:
          if temp == 1:  
            print("\nThe Yeti deals you another card.")
            card = randint(2,11)
            print(card)
          if yeti_Count < 16:
            print("\nThe Yeti draws another card.")
            yeti_Count = yeti_Count + randint(2,11)

        if temp == 1:
          card_Count = card + card_Count
        countString = str(card_Count)

        if card_Count > 21 and temp == 1:
          print("Bust!")
          temp = 2
        if yeti_Count > 21:
          print("The Yeti busted!")

        if temp == 1 and card_Count < 22:
          print(("\nYour card count is: ") + countString)
          temp = int(input("\n1 - Hit\n2 - Stand\n"))

        if ace == 1:
          if temp == 1:  
            print("\nThe Yeti deals you another card.")
            card = randint(1,10)
            print(card)
          if yeti_Count < 16:
            print("\nThe Yeti draws another card.")
            yeti_Count = yeti_Count + randint(1,10)
        elif ace == 11:
          if temp == 1:  
            print("\nThe Yeti deals you another card.")
            card = randint(2,11)
            print(card)
          if yeti_Count < 16:
            print("\nThe Yeti draws another card.")
            yeti_Count = yeti_Count + randint(2,11)

        if temp == 1:
          card_Count = card + card_Count
        countString = str(card_Count)

        if card_Count > 21 and temp == 1:
          print("Bust!")
          temp = 2
        if yeti_Count > 21:
          print("The Yeti busted!")

        if temp == 1 and card_Count < 22:
          print(("\nYour card count is: ") + countString)
          temp = int(input("\n1 - Hit\n2 - Stand\n"))
      
        if ace == 1:
          if temp == 1:  
            print("\nThe Yeti deals you another card.")
            card = randint(1,10)
            print(card)
          if yeti_Count < 16:
            print("\nThe Yeti draws another card.")
            yeti_Count = yeti_Count + randint(1,10)
        elif ace == 11:
          if temp == 1:  
            print("\nThe Yeti deals you another card.")
            card = randint(2,11)
            print(card)
          if yeti_Count < 16:
            print("\nThe Yeti draws another card.")
            yeti_Count = yeti_Count + randint(2,11)

        if temp == 1:
          card_Count = card + card_Count
        countString = str(card_Count)

        if card_Count > 21 and temp == 1:
          print("Bust!")
          temp = 2
        if yeti_Count > 21:
          print("The Yeti busted!")

        print("\nThe drawing has been completed!")
        yeti_CountStr = str(yeti_Count)
        print(("Your card count is: ") + countString)
        print(("The Yeti's card count is: ") + yeti_CountStr)
        if yeti_Count > card_Count or card_Count > 21:
          if yeti_Count < 22:
            print("Clifford wins this round!")
            tries = tries + 1
            score = score - bet
            scoreString = str(score)
        if yeti_Count < card_Count or yeti_Count > 21:
          if card_Count < 22:
            print("You win this round!")
            tries = tries + 1
            wins = wins + 1
            score = score + bet
            scoreString = str(score)
        if yeti_Count == card_Count or yeti_Count > 21 and card_Count > 21:
          print("You tied!")
          tries = tries + 1
        mode = 0
  if score > 1000 & yeti_Agg > 0:
    quit("Clifford grunts in frustration, and proceeds to stand up and crush your bones with his massive hands.")