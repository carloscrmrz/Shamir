import getopt
import sys
import inoutput.iops as io
from inoutput.cipherops import cipher_file
from inoutput.decipherops import decipher_file

def main():
    desc = "Shamir is a fast and easy way to encrypt and pass secret files."
    args = sys.argv[1:]
    opts = "hc:d:sm"
    long_opts = ["--help", "--decipher=", "--cipher=", "--shares=", "--minimum="]

    cipher_decipher_flag = ""
    path_to_file = ""
    path_to_shares = ""
    shares = 5
    minimum = 3

    try:
        arguments, values = getopt.getopt(args, opts, long_opts)
        for currentArg, currentVal in arguments:
            if currentArg in ("-h", "--help"):
                show_help()
            if currentArg in ("-c", "--cipher"):
                cipher_decipher_flag = "cipher"
                path_to_file = currentVal
            if currentArg in ("-d", "--decipher"):
                cipher_decipher_flag = "decipher"
                path_to_file = currentVal
                path_to_shares = values[0]
                minimum = int(values[2])
            if currentArg in ("-s", "--shares"):
                shares = int(values[0])
                minimum = int(values[1])
            if currentArg in ("-m", "--minimum"):
                minimum = int(values[0])
                shares = int(values[1])
    except getopt.error as err:
        print(str(err))

    if (cipher_decipher_flag != "decipher"):
        if (shares < minimum):
            print("Number of minimum is less than shares")
            shares = minimum + minimum + 1

    if (cipher_decipher_flag == "cipher"):
        cipher_file(path_to_file, shares, minimum)
    elif (cipher_decipher_flag == "decipher"):
        decipher_file(path_to_file, path_to_shares, minimum)
    else:
        # Shouldn't reach here if passed any of the flags.
        print("option not recognized, check your inputs.\n")
        sys.exit(0)

main()
