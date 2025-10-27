def init_state(secret: str, max_tries: int) -> dict:
    return {
        "secret": secret,
        "display": [' _' * len(secret)],
        "guessed": {},
        "wrong_guessed": 0,
        "max_tries": max_tries
    }