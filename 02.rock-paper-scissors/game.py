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

print("Welcome to the Rock Paper Scissors game!")
choice = int(input("Choose rock (0), paper (1), or scissors (2): "))
computer_choice = random.randint(0, 2)
options = [rock, paper, scissors]
if choice < 0 or choice > 2:
    print("Not a valid choice. You lose!")
else:
    print("You chose:")
    print(options[choice])
    print("Computer chose:")
    print(options[computer_choice])
    if computer_choice == choice:
        print("It's a draw!")
    elif (choice - computer_choice) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")