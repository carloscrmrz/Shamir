from . import mod_math
import random

big_cousin = 208351617316091241234326746312124448251235562226470491514186331217050270460481

"""
  Auxiliar function that creates a random polynomial.
  @param independent the independent coefficient
  @param rank the rank of the polynomial

  @return a list of numbers that represent a polynomial
"""
def create_polynomial(independent, rank):
  return [independent] + [random.SystemRandom().randint(0, big_cousin - 1)
                                                      for i in range(rank - 1)]

"""
  Auxiliar function that handles evaluating a polynomial at a certain point.
  @param x the point to evaluate.
  @param polynomial the polynomial to evaluate.
  @param prime the number that dictates the modulo field.

  @return the evaluation of the polynomial at x.
"""
def eval_polynomial_at(x, polynomial, prime):
    acc = 0
    for coeff in reversed(polynomial):
        acc *= x
        acc += coeff
        acc %= prime
    return acc


"""
  Auxiliar function for lagrange interpolation.
  @param vals a list of numbers to multiply.

  @return the product of the list.
"""
def product_lagrange(vals):
    accum = 1
    for v in vals:
        accum *= v
    return accum

"""
  Algorithm for lagrange interpolation.
  @param x point of evaluation of lagrange interpolation.
  @param x_s list of points evaluated.
  @param y_s list of evaluations in polynomial in x.
  @param p the prime that dictates the modulo field.
"""
def lagrange_interpolation(x, x_s, y_s, p):
    k = len(x_s)

    nums = []
    denominators = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(product_lagrange((x - o for o in others)))
        denominators.append(product_lagrange((cur - o for o in others)))
    den = product_lagrange(denominators)
    num = sum([mod_math.modular_division(nums[i] * den * y_s[i] %
              p, denominators[i], p) for i in range(k)])
    return (mod_math.modular_division(num, den, p) + p) % p

