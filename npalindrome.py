# This is a problem my math teacher gave me

from math import floor, inf


def numberpalindromes(digits: int) -> float | str:
  if float(f"9e+{floor((digits+1)/2)-1}") != inf:
    return float(f"9e+{floor((digits+1)/2)-1}")
  if float(f"9e+{floor((digits+1)/2)-1}") == inf:
    return f"9e+{floor((digits+1)/2)-1}"
    
print(numberpalindromes(9101065418293857667843617946356856574656746456785835767582976387597678754765878678595878947678977893767897667689765789087654323456789087654323456786543567654323456786543234567654324567876543456786543567865434567543456543456433453456434))