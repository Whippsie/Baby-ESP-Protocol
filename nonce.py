from construct.core import *
from construct.lib import *
from binascii import hexlify
from typing import Tuple

## The section of the code that need to be updated are
## indicated with XXXX



def show_nonce(salt:bytes, seq_num:int, ext_seq:bool) -> Tuple[ bytes, dict ] :
  """shows the nonce in a binary and structure format """

  IIV_Nonce = Struct(
    ## Replace XXXX by the appropriated value which 
    ## indicates the length of the salt as 
    ## a number of bytes
    "salt" / Bytes(4),
    ## Replace the byte value taken by Const. The
    ## binary value is not correct and needs to be 
    ## replaced completely. The first  bytes have 
    ## only been indicated as an example
    ## on how to write bytes and may not be correct.
    "iv" / IfThenElse(this._.ext_seq_num_flag,
      Struct( "zero" / Const(b'\x00\x00\x00\x00'),
              "seq_num_counter" / Int32ub),
      Struct( "seq_num_counter" / Int64ub)
      )
  )

  ## defining the structure
  nonce = { 'salt' : salt, \
            'iv' : {'seq_num_counter' : seq_num } }
  try:
    ## converting structure to binary
    byte_nonce = IIV_Nonce.build(\
                   nonce, 
                   ext_seq_num_flag=ext_seq)
    ## parsing binary to structure 
    struct_nonce = IIV_Nonce.parse(\
                    byte_nonce, 
                    ext_seq_num_flag=ext_seq)
    return byte_nonce, struct_nonce
  except:
    print("\n---")
    print("> ERROR : Unable to generate the nonce")
    print("> Inputs:")
    print(">    - salt: %s"%salt)
    print(">    - sec_num: %s"%seq_num)
    print(">    - ext_seq_flag: %s"%ext_seq)
    print("-----\n")
    return None, None

    print("Nonce (structure)")
    print("    - nonce: %s" % struct_nonce)
    print("---\n")

  ## printing the different representations
  print("\n---")
  print("Inputs:")
  print("    - salt: %s"%salt)
  print("    - sec_num: %s"%seq_num)
  print("    - ext_seq_flag: %s"%ext_seq)
  print("Nonce (binary)")
  print("    - nonce [%s bytes]: %s"%(len(byte_nonce),
                                      byte_nonce))


#print(show_nonce(b'\xf7\xca\x79\xfa', 5, True)) # un num´ero de s´equence de 5 avec un num´ero de s´equence ´etendu activ´e
#print(show_nonce(b'\xf7\xca\x79\xfa', 5, False)) # un num´ero de s´equence de 5 avec un num´ero de s´equence ´etendu d´esactiv´e (cas standard)
#print(show_nonce(b'\xf7\xca\x79\xfa', 4294967295, True)) # un num´ero de s´equence de 4294967295 avec un num´ero de s´equence ´etendu activ´e
#print(show_nonce(b'\xf7\xca\x79\xfa', 4294967295, False)) # un num´ero de s´equence de 4294967295 avec un num´ero de s´equence ´etendu d´esactiv´e (cas standard)
#print(show_nonce(b'\xf7\xca\x79\xfa', 4294967296, True)) # un num´ero de s´equence de 4294967296 avec un num´ero de s´equence ´etendu d´esactiv´e (cas standard)
#print(show_nonce(b'\xf7\xca\x79\xfa', 4294967296, False)) # un num´ero de s´equence de 4294967296 avec un num´ero de s´equence ´etendu d´esactiv´e (cas standard)

#Q6
#IV est 8 bytes, soit implicite (4 zero et 4 seq number) ou 8 extended sequence number  https://www.rfc-editor.org/rfc/rfc8750.html

#Q7
