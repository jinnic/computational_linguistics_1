
"""describe the purpose of the program (see Section 4)
  
Don’t assume that just because your program passes the sample tests I provide that it
is completely correct. Come up with your own test cases and verify that the program
is producing the right output on them.

The rules of lingo are described in detail in Section 3 (“Lingo Instructions and Example Gameplay”).
"""

from getWords import getWords
from random import choice


def main() -> None:
  
  printIntro()
  all_words = getWords()
  #print( word, 'main function')
  genSecretTarget(all_words)

def printIntro():
  """Prints instructions about the game to the user."""
  print("Welcome to Lingo, a word gussing game written in python.")

def genSecretTarget(all_words: list) -> str:
  """genSecretTarget() takes list of valid words and returns randomly chosen string for current game.

  Arg: 
    allWords (list): list of valid words from wordsclean.txt

  Return:
    str: a string containing the (randomly chosen) secret target word for the current run of the game.
  """
  secret_target = choice(all_words)
  print(secret_target)
  return secret_target #choice(all_words)
  

def getGuess(all_words: list):
  print("")

def printStatus(guess, secret):
  print("")
  
def exactMatch(statusList, secretList):
  print("exactMatch")

def inexactMatch(statusList, secretList):
  print("")

main()