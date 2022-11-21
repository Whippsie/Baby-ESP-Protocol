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
  len_left = data_len % 255
  #elen = 1 + (len(line) - 1) % N
  #line += bytes(elen for _ in range(elen))
  #bytes += "\0"*len_diff
  padding_bytes += "\" + i * len_left
  nums = [1, 2, 3, 4, 5]
  for i in range(len_left):
    nums i = i+1
  padding_bytes = bytes(nums)
  print(bytes(nums))
  return padding_bytes
  ##END_CODE

