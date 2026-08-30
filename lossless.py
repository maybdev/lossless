chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \n'
base = len(chars)
map = {char:index for index,char in enumerate(chars)}

def toint(s:str)->int:
    n=-1
    for char in reversed(s):
        remainder=map[char]
        n=(n+1)*base+remainder
    return n

def tostr(n:int)->str:
    string=[]
    while n>=0:
        n,remainder=divmod(n,base)
        string.append(chars[remainder])
        n-=1
    return ''.join(string)

def pack(n:int)->bytes:
    return n.to_bytes((n.bit_length()+7)//8,'big')

def unpack(b:bytes)->int:
    return int.from_bytes(b,'big')

#------------------------------------------------------------------------------------------------

string = "Hello, World!" # Longer strings means more characters saved

integer = toint(string) # String to integer

packed = pack(integer) # Pack the integer

import sys;sys.set_int_max_str_digits(100000000) # So that big integers can be printed
print(f'\n\x1b[96mUntouched string\x1b[0m: \x1b[94m{string}\x1b[0m (\x1b[95mlen \x1b[91m{len(string)}\x1b[0m)\n\n\x1b[96mString in integer form\x1b[0m: \x1b[92m{integer}\n\n\x1b[96mInteger in byte form\x1b[0m: \x1b[93m{packed}\x1b[0m (\x1b[95mlen \x1b[91m{len(packed)}\x1b[0m)\n\n\x1b[96mCharacters saved\x1b[0m: \x1b[91m{len(string)-len(packed)} \x1b[95mchars\n\n\x1b[96mDecompressed string\x1b[0m: \x1b[94m{tostr(unpack(packed))}\x1b[0m\n')
