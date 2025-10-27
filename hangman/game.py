def init_state(secret: str, max_tries: int) -> dict:
    return {
        "secret": secret,
        "display": [' _' * len(secret)],
        "guessed": {},
        "wrong_guessed":  0,
        "max_tries": max_tries
    }

def validate_guess (ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) == 1 and ch.isalpha():
        if ch not in guessed:
            return True , " The guess was successful "
        else:
            return False , " The guess was unsuccessful "
    else:
        return False , " Invalid character entered "
    
def apply_guess (state: dict, ch: str) -> bool:
    if ch in state["secret"]:
        return True
    else:
        return False
    
def is_won (state: dict) -> bool:
    if "_" not in state["display"]:
        return True
    
def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True