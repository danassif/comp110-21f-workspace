"""Repeating a beat in a loop."""

__author__ = "730243388"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
<<<<<<< HEAD
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
=======
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0
if (number < 1):
    print("No beat...")
else:
    print_beat = beat
    while (i < number - 1):
        print_beat += "" + beat

    print(print_beat)
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
