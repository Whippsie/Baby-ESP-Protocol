import json
from base64 import b64encode

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from binascii import hexlify
from typing import Tuple
import pprint
def bitstring_to_bytes(s):
  v = int(s, 2)
  b = bytearray()
  while v:
    b.append(v & 0xff)
    v >>= 8
  return bytes(b[::-1])

def nonce_info( cipher )-> Tuple[ bytes, int ]:
  """returns nonce value and nonce length """
  ## BEGIN CODE TO BE CHANGED
  nonce = cipher.nonce
  nonce_len = 16 #normalement 12, mais ici par défaut c'est 16 (voir doc)
  ## END CODE TO BE CHANGED
  return nonce, nonce_len 

print( "================================================" )
print( "====== Alice and Bob Secure Communication ======" )
print( "================================================" )
## secret key shared by Alice and Bob
key = get_random_bytes(16)

## Alice
alice_plaintext = b"secret"
print("Alice plaintext is: %s"%alice_plaintext)
##    - 1. initilaization of the cipher
alice_cipher = AES.new(key, AES.MODE_GCM,\
                       nonce=None, mac_len=16)
##    - 2. encryption, authentication
ciphertext, icv = \
  alice_cipher.encrypt_and_digest(alice_plaintext)

print( "The encrypted message sent by Alice to Bob is:" )
print( f"    - ciphertext: {hexlify( ciphertext, sep=' ' )}" ) 
print( f"    - icv: {hexlify(icv, sep=' ' )}" )
nonce, nonce_len = nonce_info( alice_cipher )
print( f"    - nonce [{nonce_len} bytes ]: {hexlify( nonce, sep=' ' )}" )

## Bob
bob_cipher = AES.new(key, AES.MODE_GCM,\
                     nonce=nonce,\
                     mac_len=16)

bob_plaintext = \
  bob_cipher.decrypt_and_verify(ciphertext, icv)
print("Bob plaintext is: %s"%bob_plaintext)

## secret key shared by Alice and Bob
key = b'\xf1\x6a\x93\x0f\x52\xa1\x9b\xbe\x07\x1c\x6d\x44\xb4\x24\xf3\x03'
nonce_dict = {
  'nonce_0': b'\0' * 16, \
  'nonce_1': b'\0' * 12, \
  'nonce_2': bitstring_to_bytes("00000001")*16, \
  'nonce_3': bitstring_to_bytes("00000001")*12 }
clear_text = "secret"


def encrypt_and_digest( key:bytes, nonce_dict:dict, clear_text:bytes ) -> dict:
  output_dict = {}
  for keydict in nonce_dict:
    current_nonce = nonce_dict[keydict]
    alice_cipher = AES.new(key, AES.MODE_GCM, nonce=current_nonce, mac_len=16)
    ciphertext, icv = alice_cipher.encrypt_and_digest(clear_text)
    output_dict[keydict] = (current_nonce,ciphertext, icv)

  return output_dict

print("=============TESTING QUESTION 3====================")
pprint.pprint(encrypt_and_digest(key, nonce_dict, str.encode(clear_text)))
#Q2
#Paramètres fournis pour
"""
alice_cipher = AES.new(key, AES.MODE_GCM,\
                       nonce=None, mac_len=16)
key (aléatoire à chaque exécution)
type (change pas)
nonce (aléatoire à chaque exécution)
longueur mac(change pas)
icv pas sure? vérifier avec la variable ciphertext
https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#gcm-mode
"""
"""
=============TESTING QUESTION 3====================
{'nonce_0': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
             b'\xc5\x80i\x1e\x88\xd4',
             b'\xad\x04\xaa\x89%\x14fr&\x9dB\\:j\xd3\x1c'),
 'nonce_1': (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
             b'r\xff\\\xdc\xae\x99',
             b'\x7f\xf2\x92}\xcb\xf4\xaf\x9bD_ \xb1)\xacs\xa5'),
 'nonce_2': (b'\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01',
             b'-`\xd489\xaf',
             b'a!|F\xfa\xc9]\xc7\xe5\xec\xe4\xc3\x81\xf9\xe2\x06'),
 'nonce_3': (b'\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01',
             b'\xdb\x10`\xf3\xf5Q',
             b'%\x80\xf0\xc6\x89\xd2`5\x7f3L\x9b\x85\xd5/\xd9')}
"""

