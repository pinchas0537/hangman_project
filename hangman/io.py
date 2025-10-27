def prompt_guess() -> str:
    return input("Please enter a letter to guess: ")

def print_status(state: dict) -> None:
    print(f"""The word is: {state["display"]}\n 
          All the letters guessed are: {state["guessed"]}
          The remaining guesses are: {state["max_tries"] - {state["wrong_guessed"]}}
          """)