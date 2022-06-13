from Cryptodome.Cipher import AES
from Cryptodome import Random
from hashlib import md5
from os import urandom

"""
  Auxiliar function that handles the formatting of our password, it 
  also encrypts it for more security (even though its on md5)
  @param password our password
  @param salt a salt to protect our hash
  @param key_length the length of the key
  @param iv_length the length of our blocks.

  @return a tuple of bytes, for use in encrypting.
"""
def derive_key_and_iv(password, salt, key_length, iv_length):
    d = d_i = b''
    while len(d) < key_length + iv_length:
        d_i = md5(d_i + str.encode(password) + salt).digest() 
        d += d_i
    return d[:key_length], d[key_length:key_length+iv_length]    

"""
  Function that handles the logic of encoding our file
  @param in_file the file to be encrypted.
  @param out_file the file where our encrypted file will be saved.
  @param password the password to lock the file.
  @key_length the length of the key to be used in AES.
"""
def encrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size 
    salt = urandom(bs) 
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    out_file.write(salt)
    finished = False

    while not finished:
        chunk = in_file.read(1024 * bs) 
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = (bs - len(chunk) % bs) or bs
            chunk += str.encode(padding_length * chr(padding_length))
            finished = True
        out_file.write(cipher.encrypt(chunk))

"""
  Function that handles decripting.
  @param in_file the path to the encrypted file
  @param out_file the path to the file where our decrypted file will be saved.
  @param password the password to unlock our file.
  @key_length the length of the key/password in bytes.
"""
def decrypt(in_file, out_file, password, key_length=32):
    bs = AES.block_size
    salt = in_file.read(bs)
    key, iv = derive_key_and_iv(password, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
        if len(next_chunk) == 0:
            padding_length = chunk[-1]
            chunk = chunk[:-padding_length]
            finished = True 
        out_file.write(bytes(x for x in chunk)) 
