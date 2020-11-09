import random


# Functions
def stringMaker(lst):
    x = ''
    for i in lst:
        x += i
    return x


# The Game
print("Welcome to our game of guessing.\nYou have to guess the letters of the name given to you.\nYou have 10 tries "
      "only.\nIt's your turn to win now.\nGood Luck!\n")

secret_words = ["person", "world", "apple", "hand", "woman", "place"]
word = random.choice(secret_words)

word_to_fill = []
for i in word:
    word_to_fill.append("_")

letter = random.choice(word)

for i in range(len(word)):
    if word[i] == letter:
        word_to_fill[i] = letter

for i in range(10):
    if stringMaker(word_to_fill) == word:
        break
    print(stringMaker(word_to_fill))
    print(10 - i, " tries left")

    guess = str(input("Guess a Character: ")).lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_to_fill[i] = guess
        print("Correct Guess\n")
    else:
        print("Wrong Guess\n")
if stringMaker(word_to_fill) == word:
    print(word, "\n")
    print("You won !!")
else:
    print(word, "\n")
    print("You lose !!")
