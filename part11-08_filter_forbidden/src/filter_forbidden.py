# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return "".join([cha for cha in list(string) if cha not in forbidden])
