def prompt_guess() -> str:
    return input("Please enter a letter to guess: ")

def print_status(state: dict) -> None:
    print(f"""The word is: {state["display"]}\n 
          All the letters guessed are: {state["guessed"]}
          The remaining guesses are: {state["max_tries"] - {state["wrong_guessed"]}}
          """)

def print_result(state: dict) -> None:
    if "_" not in state["display"]:
        print("You won!")
    else:
        print("Unfortunately, you didn't win!")
    print(f'''The chosen word is: {state["secret"]}.
              The letters you guessed are: {state["guessed"]}.''')