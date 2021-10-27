"""Repeating a beat in a loop."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
number: str = input("How many times do you want to repeat it? ")
final: str = ""
i: int = 0
if int(number) <= 0:
    print("No beat...")

while i < int(number) - 1:
    final = beat + " " + final
    i += 1

final += beat
print(final)
