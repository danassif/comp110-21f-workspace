"""Finding duplicate letters in a word."""

__author__ = "123456789"

word: str = input("Enter a word: ")
<<<<<<< HEAD
duplicate: bool = False

i: int = 0

while i < len(word):
    char: str = word[i]
    j: int = i + 1
    while j < len(word):
        if word[j] == char:
=======

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
            duplicate = True
        j += 1
    i += 1

<<<<<<< HEAD
print("Found duplicate: " + str(duplicate))
=======
print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
