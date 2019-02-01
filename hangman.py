# Welcome to me dipping my toes into python!

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
# ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
# ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
# ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
# ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
# ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random as r

words = [
  "algorithm", "binary", "computer",
  "development", "encryption", "freeware",
  "gigabyte", "hardware", "integer",
  "java", "kernel", "linux",
  "mainframe", "network", "online",
  "protocol", "queue", "reboot",
  "syntax", "terminal", "unix",
  "virus", "website"
]

def getWord():
  num = r.randint(0, len(words) - 1)
  return words[num]

def checkAnswer(guess, letters):
  index = 0
  for l in letters:
    if guess == l:
      return True
    index += 1
  return False

def updateDisplay(guess, dashes, letters):
  index = 0
  for l in letters:
    if guess == l:
      dashes[index] = guess
    index += 1
  return dashes

def init():
  print("Welcome to Hangman (python edition)!")
  game = True
  guesses = 5
  word = getWord()
  letters = []
  dashes = []
  for w in word:
    letters.append(w)
    dashes.append("_")
  print(letters)
  while game == True:
    print(" ".join(dashes));
    print("guesses remaining:", guesses)
    guess = input("enter a letter:\n")
    check = checkAnswer(guess, letters)
    if check:
      dashes = updateDisplay(guess, dashes, letters)
      try:
        dashes.index("_")
      except:
        game = False
        print("Congratulations! You got the word!")
        print("Thanks for playing :]")
    else:
      guesses -= 1
      if guesses == 0:
        game = False
        print("Ahh, better luck next time.")
        init()

init()
