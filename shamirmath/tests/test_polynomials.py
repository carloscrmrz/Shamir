import shamirmath.polynomials as poly

def test_polynomial_rank_is_minimum():
  rank = 5

  # Polynomial has less rank than expected
  polynomial = poly.create_polynomial(1, 2)
  assert len(polynomial) != rank

  # Polynomial must have the same rank
  polynomial = poly.create_polynomial(1, rank)
  assert len(polynomial) == rank

def test_eval_polynomial():
  poly_1 = [-1, 1, 1] # f(x) = x^2 + x - 1
  assert poly.eval_polynomial_at(1, poly_1, 1000000) == 1 # We use this value for prime only for convenience
  assert poly.eval_polynomial_at(0, poly_1, 1000000) == 999999
  assert poly.eval_polynomial_at(-10, poly_1, 1000000) == 89
  assert poly.eval_polynomial_at(5, poly_1, 1000000) == 29

  poly_2 = [100] # f(x) = 100
  assert poly.eval_polynomial_at(0, poly_2, 100000) == 100
  assert poly.eval_polynomial_at(1, poly_2, 100000) == 100
  assert poly.eval_polynomial_at(10000, poly_2, 100000) == 100
  assert poly.eval_polynomial_at(5555, poly_2, 100000) == 100

def test_product_lagrange():
  assert poly.product_lagrange([1,2,3]) == 6
  assert poly.product_lagrange([1,2,3,4,5]) == 120
  assert poly.product_lagrange([]) == 1

def test_lagrange_interpolation():
  x_s = [1,2,3,4,5]
  y_s = [86,105,176,359,738]

  assert poly.lagrange_interpolation(0, x_s, y_s, 1000000) == 684416
  assert poly.lagrange_interpolation(1, x_s, y_s, 1000000) == 44032
  assert poly.lagrange_interpolation(2, x_s, y_s, 1000000) == 13440




