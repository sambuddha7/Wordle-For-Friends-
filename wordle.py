from colorama import Fore
from letter import Letter
class Wordle:
  def __init__(self, secret: str):
    self.secret: str = secret.upper() 
    self.words_guessed = []
    self.colored_guesses = []
    self.attempts_left = 6
    self.dictionary = {}
    for c in self.secret:
      if c in self.dictionary:
        self.dictionary[c] += 1
      else:
        self.dictionary[c] = 1
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
    guess_dict = {}
    #dictionary to compare occurences of letter with the secret word
    for i in range(5):
      if word[i] in guess_dict:
        guess_dict[word[i]] += 1
      else:
        guess_dict[word[i]] = 1
    for i in range(5):
      letter = Letter(word[i])
      letter.position = word[i] == self.secret[i]
      if word[i] in self.secret and guess_dict[word[i]] == self.dictionary[word[i]]:
        letter.contains = True
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
      joined = " ".join(result_with_color)
    self.colored_guesses.append(joined)
    return self.colored_guesses
    # for c in self.colored_guesses: #printing the colored letters
    #   print(c)
    # for i in range(self.attempts_left): #printing the blank spaces
    #   print(('_ ' * 5) + "\n")
  def draw_box(self, colored_guesses):
    char = 9 #5 letters + 4 spaces
    padding = 2
    top_border = '┌' + ('─' * char) + '┐'
    print(top_border)
    for c in self.colored_guesses:
      middle = '│' + c + '│'
      print(middle)
    for i in range(self.attempts_left): #printing the blank spaces
      middle =  '│' + ('_ ' * 4) + '_│'
      print(middle)
    bottom_border = '└' + ('─' * char) + '┘'
    print(bottom_border)
    