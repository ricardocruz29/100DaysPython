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

moves = [rock,paper,scissors]

#User choice
move_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
#Verification
if 0 < move_index or move_index > 2:
    print("Invalid number. You lose")
    exit()
#Computer choice
move_random_index = random.randint(0,2)

print(f"User chose {moves[move_index]}")
print(f"Computer chose {moves[move_random_index]}")

#Rock win Scissors, lose Paper
#Paper win Rock, lose Scissors
#Scissors win Paper, lose Rock

#Same move
if move_index == move_random_index:
    print("You draw")
#User Rock and Computer Scissors
elif move_index == 0 and move_random_index == 2:
    print("You win")
#User Scissors and Computer Rock
elif move_index == 2 and move_random_index == 0:
    print("You lose")
#General moves, that happend with the 2 exceptions above
elif move_index < move_random_index:
    print("You lose")
elif move_index > move_random_index:
    print("You win")

