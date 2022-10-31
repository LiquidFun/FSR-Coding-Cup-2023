import string
import sys

alphabet = set(string.ascii_lowercase)
book_letters = set(sys.stdin.read())

print("valid" if alphabet - book_letters else "invalid")
