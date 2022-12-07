from construct.core import *
from construct.lib import *

#0 à 255 octets suivi du pad length et next header
#chaque byte a 0 à 255 valeur
#le padding est 1,2,3,4...
"""
   The Next Header is an 8-bit field that identifies the type of data
   contained in the Payload Data field, e.g., an extension header in
   IPv6 or an upper layer protocol identifier.  The value of this field
   is chosen from the set of IP Protocol Numbers defined in the most
   recent "Assigned Numbers" [STD-2] RFC from the Internet Assigned
   Numbers Authority (IANA).  The Next Header field is mandatory."""
def pad( data_len ):
  """ return the Padding field 

  Args:
    data_len: the length of the Data Payload 
  """
  ### Complete the code so it returns the necessary 
  ### padding bytes for an ESP packet. The padding 
  ### bytes are derived from data_len the length 
  ### expressed in number of bytes of the Data 
  ### Payload 

  ##BEGIN_CODE
  #pair
  if (data_len % 2==0):
      len_left = (data_len+2) % 4
  else:
      len_left = data_len % 4
  padding_bytes = b'\x01\x02\x03\x04'
  padding_bytes = padding_bytes[:len_left]
  return padding_bytes
  ##END_CODE

#Test for padding
#print(pad(14))
#print(pad(15))
#print(pad(16))
#print(pad(17))
#print(pad(18))
#print(pad(19))
#print(pad(20))
#print(pad(0))
#print(pad(2))
#print(pad(1))

