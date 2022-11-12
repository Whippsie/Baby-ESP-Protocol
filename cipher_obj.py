from construct.core import *
from construct.lib import *
from binascii import hexlify
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

## The section to complete are indicated 
## with XXXX or tagged with BEGIN_CODE and
## END_CODE

## AES_GCM_16_IIV related shared context between 
## Alice and Bob. Please do not update this section
key = b'\xf1\x6a\x93\x0f\x52\xa1\x9b\xbe\x07\x1c\x6d\x44\xb4\x24\xf3\x03'
mac_len=16
ext_seq_num_flag = False
seq_num_counter = 5
salt = b'\xf7\xca\x79\xfa'



def ciphers_obj( key:bytes, mac_len:int, ext_seq_num_flag:bool, seq_num_counter:int, salt:bytes ):
  """ returns the cipher object for AES_GCM """
  ## Complete the code so the function returns the 
  ## appropriated cipher object. The purpose is to 
  ## fill XXXX with the appropriated parameters
  
  ## BEGIN_CODE
  IIV_Nonce = Struct(
    ## Replace XXXX by the appropriated value which 
    ## indicates the length of the salt as 
    ## a number of bytes
    "salt" / Bytes(XXXX),
    "iv" / IfThenElse(this._.ext_seq_num_flag,
    ## Replace the byte value taken by Const. The
    ## binary value is not correct and needs to be 
    ## replaced completely. The first  bytes have 
    ## only been indicated as an example
    ## on how to write bytes and may not be correct.
      Struct( "zero" / Const(b'XXXXXXXXX'),
              "seq_num_counter" / Int32ub),
      Struct( "seq_num_counter" / Int64ub)
      )
  )

  return AES.new(XXX)
  ## END_CODE


## Alice
alice_plaintext = b"yet another secret"
print("Alice plaintext is: %s"%alice_plaintext)
alice_cipher = ciphers_obj()
## encryption, authentication
ciphertext, icv =\
  alice_cipher.encrypt_and_digest(alice_plaintext)
nonce = alice_cipher.nonce
print("The encrypted message sent by Alice to Bob is:")
print(" - (nonce [%s]: %s,"%(len(nonce), 
                             hexlify(nonce)))
print(" - ciphertext: %s"%hexlify(ciphertext))
print("icv[%s]: %s"%(len(icv), hexlify(icv)))


## Bob
bob_cipher = AES.new(key, AES.MODE_GCM,\
                     nonce=nonce, mac_len=mac_len)
### verification, decryption
bob_plaintext = \
  bob_cipher.decrypt_and_verify(ciphertext, icv)
print("Bob plaintext is: %s"%bob_plaintext)

