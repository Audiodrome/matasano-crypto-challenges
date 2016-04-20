import binascii
import base64

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

unHex = binascii.unhexlify(hex)

print unHex

base_sixtyfour = base64.b64encode(unHex)

print base_sixtyfour

