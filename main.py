import random
from art import logo
from replit import clear

def card_generator():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(score):
  if sum(score) == 21 and len(score) == 2:
    return 0
  if 11 in score and sum(score) > 21:
    score.remove(11)
    score.append(1)
  
  return sum(score)

def who_win(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You got more than 21. you lose"
  elif user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "lose, computer has BlackJack "
  elif user_score == 0:
    return "Win, you got BlackJack"
  elif user_score > 21:
    return "You got more than 21. You lose"
  elif computer_score > 21:
    return "Computer has more than 21, You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"
  
def game_engine():
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False
  for i in range(2):
    user_cards.append(card_generator())
    computer_cards.append(card_generator())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards {user_cards}, current score {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      call = input("Type 'y' to get anothe card or type 'n' to pass.")
      if call == "y":
        user_cards.append(card_generator())
      else:
        game_over = True
  
  
  
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(card_generator())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards}, and your final score {user_score}")
  print(f"  Computer final hand: {computer_cards}, and computer final score {computer_score}")
  print(who_win(user_score, computer_score))

while input("Do you want o play a game of BlackJack? Type 'y' or 'n': ") == "y":
  clear()
  
  game_engine()

