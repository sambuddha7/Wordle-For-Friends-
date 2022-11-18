from colorama import Fore
from letter import Letter
class Wordle:
  def __init__(self, secret: str):
    self.secret: str = secret.upper() 
    self.words_guessed = []
    self.colored_guesses = []
    self.attempts_left = 6
    pass
  def is_solved(self):
    if len(self.words_guessed) > 0 and self.words_guessed[-1] == self.secret:
      return True
    else: return False
  
  def can_attempt(self)->bool:
     return self.attempts_left > 0 and not self.is_solved()
  
  def attempt(self, word: str):
    self.attempts_left -= 1
    word = word.upper()
    self.words_guessed.append(word)
  
  #makes letter objects of every letter in the word
  def guess(self, word: str):
    result = []
    word = word.upper()
    for i in range(5):
      letter = Letter(word[i])
      letter.position = word[i] == self.secret[i]
      letter.contains = word[i] in self.secret
      result.append(letter)
    return result
  #traverses through the word and prints out colored letters
  def guesses(self, word: str):    
    result = self.guess(word)
    result_with_color = []
    for l in result:
      if l.position: 
        color = Fore.GREEN
      elif l.contains: 
        color = Fore.YELLOW
      else: 
        color = Fore.WHITE
      colored_letter = color + l.char + Fore.RESET
      result_with_color.append(colored_letter)
      joined = "".join(result_with_color)
    self.colored_guesses.append(joined)
    for c in self.colored_guesses:
      print(c)
    for i in range(self.attempts_left):
      print(('_' * 5) + "\n")