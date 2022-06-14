import ast
import sys
import shamirmath.polynomials as poly
from . import iops as io


big_cousin = 208351617316091241234326746312124448251235562226470491514186331217050270460481

"""
 Auxiliar function to convert strings directly into tuples.
 @param string the string to be converted into a tuple.

 @return the parsed tuple
"""
def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return

"""
 Function that deciphers an AES file with the correct amount of shares, if 
 not provided the correct amount of shares the program will shutdown.
 @param path_to_file the path to our AES file.
 @param path_to_shares the path to our shares file.
 @param minimum the minimum needed shares.
"""
def decipher_file(path_to_file, path_to_shares, minimum):
    path_to_file = path_to_file[:len(path_to_file) - 4]
    shares_list = []
    with open(path_to_shares) as file:
        for line in file:
            shares_list.append(parse_tuple(line))
    try: 
        password = recover_secret(shares_list, minimum)
    except:
        print(f"need at least {minimum} shares")
        sys.exit(-1)

    with open(f"{path_to_file}.aes", "rb") as in_file, open(f"{path_to_file}", "wb") as out_file:
        io.decrypt(in_file, out_file, password)

"""
 Auxiliar function that helps us recover the hash of our password, only works
 when the minimum number of shares is satisfied.
 @param shares the list with shares.
 @param minimum the minimum number of shares.
 @param prime a prime number if we decide to provide our own.
"""
def recover_secret(shares, minimum, prime=big_cousin):
    if len(shares) < minimum:
        raise ValueError()
    x_s, y_s = zip(*shares)
    return hex(poly.lagrange_interpolation(0, x_s[:minimum], y_s[:minimum], big_cousin))[2:]
