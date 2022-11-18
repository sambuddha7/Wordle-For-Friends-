from wordle import Wordle
import random
import getpass
def main():
    print("Wordle For Friends!\n")
    print("Pass a secret 5 letter word for your friend to guess!\n")
    print("Or type 'R' for a random word\n")
    data_src = "dataset/five_letter_words.txt"
    data_set = data_to_sets(data_src)
    
    #sec = input("Type Secret Word:").upper()
    sec = getpass.getpass(prompt = "Type Secret Word:").upper()
    if sec == 'R':
      sec = random.choice(list(data_set))
    while len(sec) != 5 or sec not in data_set or sec == 'R':
      if sec == 'R':
        sec = random.choice(list(data_set))
      sec = getpass.getpass(prompt = "Word must be a valid 5 letter english word:").upper()
    
    wordle = Wordle(sec)
    while wordle.can_attempt():
        inp = input("Enter guess:")
        if len(inp) != 5:
          print("Enter input of correct length")
          continue
        if inp.upper() not in data_set:
          print("Not in word list\n")
          continue
        wordle.attempt(inp)
        wordle.draw_box(wordle.guesses(inp))
        
    if wordle.is_solved():
      print("You guessed the word!")
    else: 
      print("Attempts over! Better luck next time:(") 
      print(f"The word was: {wordle.secret}")

def data_to_sets(path:str):
  word_set = set()
  with open(path, "r") as f:
    for line in f.readlines():
      word = line.strip().upper()
      word_set.add(word)
  return word_set
if __name__ == "__main__":
    main()