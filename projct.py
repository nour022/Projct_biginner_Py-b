from art import logo
import random
# list of numbers
numbers = []
for item in range(101):
    numbers.append(item)


def easy_level():
    num = random.choice(numbers)
    for i in range(11):
        print(f"You have {10-i} attempts remaining to guess the number.")
        m_guess = int(input("Make a guess: "))
        print(f"number is {num}")
        if m_guess == num:
            print("you win the game")
            return 0
        elif i == 10:
            print("you lose the game")
            return 0


def hard_level():
    num = random.choice(numbers)
    for i in range(6):
        print(f"You have {5-i} attempts remaining to guess the number.")
        m_guess = int(input("Make a guess: "))
        print(f"number is {num}")
        if m_guess == num:
            print("you win the game")
            return 0
        elif i == 5:
            print("you lose the game")
            return 0
        if num < m_guess:
            print("To heigth")
        else:
            print("to lowe")


print(logo)
run = True
print('Welcom to the Number Guessing Game! \n')
print("I'm thinking of a number between 1 aand 100.")
while run:
    ask = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if ask == "easy":
        easy_level()
    else:
        hard_level()
    runs = input("This repl has exied, run again?: 'y' or 'n'")
    if runs == 'n':
        print("good bye")
        run = False
