import inoutput.cipherops as cipher

def test_minimum_morethan_total():
  minimum = 10
  shares = 5 
  # Here we assert that if min > shares then we don't create shares
  try:
    cipher.create_shares(1, minimum, shares)
  except:
    assert True
  
  # Now we make min < shares
  minimum, shares = shares, minimum

  try:
    cipher.create_shares(1, minimum, shares)
  except:
    # Shouldn't reach here
    assert False
  assert True

def test_shares_number():
  number_shares = 5
  independent = 10

  test_shares = cipher.create_shares(independent, 1, 2)
  assert len(test_shares) != number_shares

  test_shares = cipher.create_shares(independent, 1, number_shares)
  assert len(test_shares) == number_shares

def test_hashed():
  password = "hello".encode('utf-8')
  hashed_pass = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

  hash = cipher.hash_password(password).hex()
  assert hashed_pass == hash
