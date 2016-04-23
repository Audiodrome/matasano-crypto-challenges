import binascii
import base64

hex = "1c0111001f010100061a024b53535009181c"
xor_against = "686974207468652062756c6c277320657965"

unHex = binascii.unhexlify(hex)
#unHex2 = binascii.unhexlify(xor_against)

print type(unHex)


#xor_result = (unHex ^ xor_against)

#print xor_result

#print (unHex^xor_against)



