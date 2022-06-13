from . import mod_math


def eval_polynomial_at(x, polynomial, prime):
    acc = 0
    for coeff in reversed(polynomial):
        acc *= x
        acc += coeff
        acc %= prime
    return acc


def product_lagrange(vals):
    accum = 1
    for v in vals:
        accum *= v
    return accum


def lagrange_interpolation(x, x_s, y_s, p):
    k = len(x_s)

    nums = []
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(product_lagrange((x - o for o in others)))
        dens.append(product_lagrange((cur - o for o in others)))
    den = product_lagrange(dens)
    num = sum([mod_math.modular_division(nums[i] * den * y_s[i] %
              p, dens[i], p) for i in range(k)])
    return (mod_math.modular_division(num, den, p) + p) % p
