import binascii
import base64
import sys

str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"

s1 = binascii.unhexlify(str1)
s2 = binascii.unhexlify(str2)

s1 = int.from_bytes(s1, byteorder = sys.byteorder)
s2 = int.from_bytes(s2, byteorder = sys.byteorder)

xor_d = s1 ^ s2

xor_d = xor_d.to_bytes((xor_d.bit_length() // 8) + 1,
                       byteorder = sys.byteorder)

result = base64.b16encode(xor_d)

print (result)

