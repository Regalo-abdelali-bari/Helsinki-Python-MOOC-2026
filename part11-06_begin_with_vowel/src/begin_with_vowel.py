# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    return [word for word in words if word.lower().startswith(("a","e","i","o","u"))]

