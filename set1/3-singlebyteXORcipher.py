import base64
import binascii
import sys
import string

hexEncodeStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

hexEncodeStr = binascii.unhexlify(hexEncodeStr)
s1 = int.from_bytes(hexEncodeStr, byteorder = sys.byteorder)


for i in string.ascii_letters:
    #print (i)
    alpha = i*len(hexEncodeStr)
    print (bytes(alpha, 'ascii'))
    alpha = bytes(alpha, 'ascii')
    #alpha = binascii.unhexlify(alpha)
    #print (alpha)
    # result = base64.b16decode(alpha)
    s2 = int.from_bytes(alpha, byteorder = sys.byteorder)
    # print ("S1: %s" % s1)
    # print ("S2: %s" % s2)
    #print (s1)
    #print (s2)
    xord = s1 ^ s2
    xord = xord.to_bytes((xord.bit_length() // 8) + 1,
                          byteorder = sys.byteorder)
    print (xord)
    #result = base64.b16encode(xord)
    #print (result)

# import string

# h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# hh = bytes.fromhex(h)

# for i in string.ascii_letters:
#     print(type(i*len(hh)))

# h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# hh = bytes.fromhex(h)
    
# for k in string.ascii_letters:
#     print(k)
#     print(bytes([a^b for (a,b) in zip(hh,bytes(k*len(hh),'ascii'))]))
