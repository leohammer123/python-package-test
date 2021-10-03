from Crypto import Util
from Crypto.Util.number import *
flag = """flag{math_is_harder_than_you_thought}""".encode()
flag = bytes_to_long(flag)
a = 1345212
b = 123456
c = 13378

def encrypt(flag):
    ans = flag**2*a+flag*b+13378
    return ans


print(encrypt(flag))
