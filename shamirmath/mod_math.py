def extended_gdc(a,b):
  x = 0
  prev_x = 1
  y = 1
  prev_y = 0

  while b != 0:
    quotient = a // b
    a,b = b, a % b
    x, prev_x = prev_x - quotient * x, x
    y, prev_y = prev_y - quotient * y, y
  return prev_x, prev_y

def modular_division(a, b, prime):
  inverse, _ = extended_gdc(b, prime)
  return a * inverse