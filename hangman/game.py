guessed = {}
wrong_guessed = 0
display = []

def init_state(secret: str, max_tries: int) -> dict:
    return {
        "secret": secret,
        "display":[' _' * len(secret)],
        "guessed":guessed,
        "wrong_guessed":wrong_guessed,
        "max_tries": max_tries
    }