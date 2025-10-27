def init_state(secret: str, max_tries: int) -> dict:
    return {
        "secret": secret,
        "display":[' _' * len(secret)],
        "guessed":set[str],
        "wrong_guessed":int,
        "max_tries": max_tries
    }