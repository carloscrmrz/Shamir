from hashlib import sha256
from getpass import getpass
import sys
from . import iops as io
import shamirmath.polynomials as poly

big_cousin = 208351617316091241234326746312124448251235562226470491514186331217050270460481

"""
  Auxiliar function that helps us to create our shares' list, works by creating a random 
  polynomial and then evaluating it at certain points, the evaluations are our shares.
  @param independent our hashed password, converted to int.
  @param minimum the minimum amount of shares needed.
  @param shares the amount of shares to be created.

  @return a list of tuples where each tuple is a certain evaluation of our polynomial
"""
def create_shares(independent, minimum, shares):
    if minimum > shares:
        raise Exception()

    polynomial = poly.create_polynomial(independent, minimum)
    f_x = [(i, poly.eval_polynomial_at(i, polynomial, big_cousin))
           for i in range(1, shares + 1)]

    return f_x

"""
  Auxiliar function that asks the user for a password and then hashes it, returning the hash
  in bytes.
  
  @return the hash in byte format
"""
def create_hashed_password():
  password = getpass("Please create a password: ").encode('utf-8')
  return hash_password(password)

"""
  Auxiliar functions that handles the hashing (with SHA256) of a string.
  @param password the string to be hashed

  @return the hash in byte format
"""
def hash_password(password):
  hash = sha256()
  hash.update(password)
  hash.digest()
  return hash.digest()

"""
  Principal function, handles the logic of getting the secret, then making an encrypted copy of
  our file. It also creates the file with the shares.
  @param path_to_file the path to the file to be encrypted.
  @param shares the amount of shares to be created.
  @param minimum the amount of shares required to unencrypt our file.
"""
def cipher_file(path_to_file, shares, minimum):
    formated_password = create_hashed_password()
    secret = formated_password.hex()

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