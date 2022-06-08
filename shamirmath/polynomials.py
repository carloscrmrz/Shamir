from . import mod_math

def eval_polynomial_at(x, polynomial, prime):
  acc = 0
  for coefficient in reversed(polynomial):
    acc *= x
    acc += coefficient
    acc %= prime
  return acc

def product_inputs(vals):
  acc = 1
  for v in vals:
    acc *= v
  return acc

def lagrange_interpolation(x, x_s, y_s, p):
  k = len(x_s)

  nums = []
  dens = []
  for i in range(k):
    others = list(x_s)
    current = others.pop(i)
    nums.append(product_inputs(x - a for a in others))
    dens.append(product_inputs(current - a for a in others))
  den = product_inputs(dens)
  num = sum([mod_math.modular_division(nums[i] * den * y_s[i] % p, dens[i], p) for i in range(k)])

  return (mod_math.modular_division(num,den,p) + p) % p