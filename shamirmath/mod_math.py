"""
  Auxiliar function to get the inverse of a number in a modulo field.
  @param a the number to get its inverse
  @param prime the number that dictates the field.

  @return a tuple, the first element is the inverse, second is remainder (if any).
"""
def extended_gdc(a, prime):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while prime != 0:
        quot = a // prime
        a, prime = prime, a % prime
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

"""
  Auxiliar function that lets us do division on a modulo field.
  @param a the numerator
  @param b the divisor
  @param prime the prime number that dictates the field

  @return the result of a / b in modulo field.
"""
def modular_division(a, b, prime):
    inverse, _ = extended_gdc(b, prime)
    return a * inverse
