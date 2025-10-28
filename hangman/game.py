def init_state(secret: str, max_tries: int) -> dict:
    return {
        "secret": secret,
        "display": ["_"] * len(secret),
        "guessed": set(),
        "wrong_guessed":  0,
        "max_tries": max_tries
    }

def validate_guess (ch: str ,state: dict) -> tuple[bool, str]:
    if len(ch) == 1 and ch.isalpha():
        if ch in state["secret"] and ch not in state["guessed"]:
            return True , " The guess was successful "
        elif ch not in state["secret"] and ch not in state["guessed"]:
            return False , " The guess was unsuccessful "
        elif ch in state["guessed"]:
            return False , "You have used this letter already, select again:"
    else:
        return False , " Invalid character entered "

    
def is_won (state: dict) -> bool:
    if "_" not in state["display"]:
        return True
    return False
    
def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    
def render_display(state: dict, ch) -> str:
    index = -1
    for i in state["secret"]:
        index += 1
        if i == ch:
            state["display"][index] = ch
    return state["display"]

def render_summary(state: dict) -> str:
    return f'''The secret word is: {state["secret"]}\n
             All the letters guessed are: {state["guessed"]}'''