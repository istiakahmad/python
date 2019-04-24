lst=[20,30,40,234]
print(type(lst))
b=bytes(lst)
print(b)
print(type(b))
#b[3]=22 # byte not support insert

b1=bytearray(lst)
print(type(b1))
b1[2]=33
print(b1)

