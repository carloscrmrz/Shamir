import ast
import sys
from . import iops as io
import shamirmath.polynomials as poly


big_cousin = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return

def decipher_file(path_to_file, shares, minimum):
    path_to_file = path_to_file[:len(path_to_file) - 4]
    shares_list = []
    with open(shares) as file:
        for line in file:
            shares_list.append(parse_tuple(line))
    try: 
        password = recover_secret(shares_list, minimum)
    except:
        print(f"need at least {minimum} shares")
        sys.exit(-1)

    with open(f"{path_to_file}.aes", "rb") as in_file, open(f"{path_to_file}", "wb") as out_file:
        io.decrypt(in_file, out_file, password)


def recover_secret(shares, minimum, prime=big_cousin):
    if len(shares) < minimum:
        raise ValueError()
    x_s, y_s = zip(*shares)
    return hex(poly.lagrange_interpolation(0, x_s, y_s, big_cousin))[2:]