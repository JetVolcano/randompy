# This is a problem my math teacher gave me

from math import isinf

class NP():
  def __init__(self, digits: int, print_at_start: bool = False) -> None:
    self.digits: int = digits
    self.result: float | str
    result: str = f"9e{(digits+1)//2-1}"
    if digits == 0:
      self.result = None
    if digits < 0:
      digits = abs(digits)
    if isinf(float(result)):
      self.result = result
    if isinf(float(result)) == False:
      self.result = float(result)
    if print_at_start == True:
      print(result)
  def __eq__(self, value) -> bool:
    return self.result == value
  def __or__(self, value) -> bool:
    return self.result or value
  def __str__(self) -> str:
    return str(self.result)
  def __len__(self) -> int:
    return len(self.result)
  def __repr__(self) -> repr:
    return repr({
      "digits": self.digits,
      "result": self.result
    })


NP(987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210, True)