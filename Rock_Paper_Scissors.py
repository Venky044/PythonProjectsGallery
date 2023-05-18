import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]

player_choice = int(input('what fo you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

computer_choice = random.choice(range(0, 3))

# Printing symble of User's Choice
print('you chose: ', player_choice)
print(images[player_choice])

# Printing symble of Computer Choice
print('Computer chose: ', computer_choice)
print(images[computer_choice])

# r>s, s>p, p>r = 0>2, 2>1, 1 > 0
if player_choice == computer_choice:
    print('game tied')
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print('you won')
else:
    print('you lose')
