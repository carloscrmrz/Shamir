import shamirmath.mod_math as mod

def test_extended_gdc():
  assert mod.extended_gdc(1, 2) == (1, 0)
  assert mod.extended_gdc(5, 7) == (3, -2)
  assert mod.extended_gdc(6435, 29) == (-10, 2219)
  assert mod.extended_gdc(1, 2) != (1, 5)
  assert mod.extended_gdc(4, 3) != (6, 54)

def test_modular_division():
  assert mod.modular_division(1, 1, 10) == 1
  assert mod.modular_division(22, 54, 53) == 22
  assert mod.modular_division(12, 54, 2) == 0
  assert mod.modular_division(6, 7, 6) == 6
  assert mod.modular_division(-1, 1, 10) == -1