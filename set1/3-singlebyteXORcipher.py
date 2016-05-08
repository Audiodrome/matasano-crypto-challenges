import base64
import binascii
import sys
import string

hexEncodeStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

hexEncodeStr = binascii.unhexlify(hexEncodeStr)
s1 = int.from_bytes(hexEncodeStr, byteorder = sys.byteorder)

for i in string.ascii_letters:
    alpha = i*len(hexEncodeStr)
    print (bytes(alpha, 'ascii'))
    alpha = bytes(alpha, 'ascii')

    s2 = int.from_bytes(alpha, byteorder = sys.byteorder)

    xord = s1 ^ s2
    xord = xord.to_bytes((xord.bit_length() // 8) + 1,
                          byteorder = sys.byteorder)
    print (xord)
    
    # Do not need to encode - deciphering
    # result = base64.b16encode(xord)
    # print (result)

# The following is  heavyberry's solution. Got a lot of help from him.
# http://perso.heavyberry.com/writeups/cryptopals1.html
# h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# hh = bytes.fromhex(h)
# for k in string.ascii_letters:
#     print(k)
#     print(bytes([a^b for (a,b) in zip(hh,bytes(k*len(hh),'ascii'))]))
