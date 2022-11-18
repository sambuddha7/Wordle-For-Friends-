from wordle import Wordle

def main():
    print("Wordle For Friends!\n")
    print("Pass a secret 5 letter word for your friend to guess!\n")
    sec = input("Type Secret Word:")
    wordle = Wordle(sec)
    while wordle.can_attempt():
        inp = input("Enter guess:")
        if len(inp) != 5:
          print("Enter input of correct length")
          continue
        wordle.attempt(inp)
        wordle.guesses(inp)
    if wordle.is_solved():
      print("You guessed the word!")
    else: print("Attempts over! Better luck next time:(") 


if __name__ == "__main__":
    main()