"""
Tuple value can not be  changed

"""
tpl=(40,50,40,"XYZ")
print(tpl)
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("XYZ"))

lst=[67,34,"XYZ"]
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))
print(tpl1)
#-------------------------------------

r = range(1, 15) # print 1 to 15-1 = 14
r = range(1, 15, 3) # print 1 to 15-1 = 14 with 3 steps
print(r)
for i in r:
    print(i)
