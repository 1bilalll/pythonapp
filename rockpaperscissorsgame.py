import random

print("Welcome to Rock, Paper, Scissors!")

a = int(input("Choose:\n1 = Rock\n2 = Paper\n3 = Scissors\nYour choice: "))
b = random.randint(1, 3)

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
---'    ____)____
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

if a < 1 or a > 3:
    print("Please choose a number between 1 and 3.")

else:
    print("\nYou chose:")

    if a == 1:
        print(rock)
    elif a == 2:
        print(paper)
    else:
        print(scissors)

    print("Computer chose:")

    if b == 1:
        print(rock)
    elif b == 2:
        print(paper)
    else:
        print(scissors)

    if a == b:
        print("Draw!")
    elif (a == 1 and b == 3) or \
         (a == 2 and b == 1) or \
         (a == 3 and b == 2):
        print("You Win!")
    else:
        print("You Lose!")