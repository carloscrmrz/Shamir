import inoutput.decipherops as decipher

big_cousin = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def test_parse_tuple():
  assert decipher.parse_tuple("(1,1)") == (1,1)
  assert decipher.parse_tuple("('1',1)") != (1,1)
  assert decipher.parse_tuple("(1,1)") != (2,1)
  
def test_recover_secret():
  # We will test various polynomials

  share_1 = [(1,15),(2,19),(3,25)]

  assert int(decipher.recover_secret(share_1, 3), 16) == 13
  assert int(decipher.recover_secret(share_1, 3), 16) != 1203
  assert int(decipher.recover_secret(share_1, 3), 16) \
    != "d"
  assert decipher.recover_secret(share_1, 3) \
    == "d"

  share_2 = [(1,86),(2,105), (3, 176), (4, 359), (5, 738)]
  assert int(decipher.recover_secret(share_2, 5), 16) == 83
  assert int(decipher.recover_secret(share_2, 5), 16) != 3456
  assert int(decipher.recover_secret(share_2, 5), 16) \
    != "53"
  assert decipher.recover_secret(share_2, 5) \
    == "53"


