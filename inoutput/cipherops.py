from hashlib import sha256
from getpass import getpass
import sys
from . import iops as io
import shamirmath.polynomials as poly
import random

big_cousin = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def create_shares(independent, minimum, shares):
    if minimum > shares:
        raise Exception()
    polynomial = [independent] + [random.SystemRandom().randint(0, big_cousin - 1)
                                                      for i in range(minimum - 1)]
    f_x = [(i, poly.eval_polynomial_at(i, polynomial, big_cousin))
           for i in range(1, shares + 1)]

    return f_x

def create_hashed_password():
    password = getpass("Please create a password: ").encode('utf-8')
    hash = sha256()
    hash.update(password)
    hash.digest()
    return hash.digest()


def cipher_file(path_to_file, shares, minimum):
    formated_password = create_hashed_password()
    secret = formated_password.hex()

    print(secret)
    try:
      user_shares = create_shares(int(secret, 16) % big_cousin, minimum, shares)
    except:
      print("The number of minimum shares can't be more than the total shares.\n")
      sys.exit(0)

    with open(f"{path_to_file}", "rb") as in_file, open(f"{path_to_file}.aes", "wb") as out_file:
        io.encrypt(in_file, out_file, secret)

    f = open(f"{path_to_file}.frg", "w")
    for share in user_shares:
      f.write(str(share) + "\n")
    f.close()