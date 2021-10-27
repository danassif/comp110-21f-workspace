"""My code for the EX01 - Numeric Operators."""

__author__ = "730335247"

left_hand: str = input("Left-hand side: ")
right_hand: str = input("Right-hand side: ")
rh_int = int(right_hand)
lh_int = int(left_hand)
print(left_hand + " ** " + right_hand + " is " + str(lh_int ** rh_int))
print(left_hand + " / " + right_hand + " is " + str(lh_int / rh_int))
print(left_hand + " // " + right_hand + " is " + str(lh_int // rh_int))
print(left_hand + " % " + right_hand + " is " + str(lh_int % rh_int))