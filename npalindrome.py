# This is a problem my math teacher gave me

from math import floor, isinf


def numberpalindromes(digits: int) -> float | str | None:
  if digits == 0:
    return None
  if digits < 0:
    digits = abs(digits)
  result: float = float(f"9e+{floor((digits+1)/2)-1}") 
  if isinf(result) == False:
    return float(f"9e+{floor((digits+1)/2)-1}")
  if isinf(result):
    return f"9e+{floor((digits+1)/2)-1}"

print(numberpalindromes(0))