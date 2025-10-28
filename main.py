from hangman import game , io
from data import words
from random import choice

def play (words: list[str], max_tries: int = 2) -> None:
    word = choice(words)
    state = game.init_state(word,max_tries)
    io.print_status(state)
    while state["wrong_guessed"] < max_tries and game.is_won(state) == False:
        input_ch = io.prompt_guess()
        validate_guess = game.validate_guess(input_ch , state["guessed"], state)
        if validate_guess[0] == False:
            state["guessed"].add(input_ch)
            state["wrong_guessed"] += 1
            print(validate_guess[1])
        else:
            state["guessed"].add(input_ch)
            print(validate_guess[1])
            swap_display = game.render_display(state,input_ch)
        io.print_status(state)
        if game.is_won(state) == True or state["wrong_guessed"] == max_tries:
            io.print_result(state)
            
            
if __name__ == "__main__":
   play(words.word)           