s={10,20,30,"XYZ",10,20,10}
print(s) # no duplicate value print

s.update([88,99])
print(type(s))
print(s) # position random

#print(s[3:5]) # not supported
#print(s*3) # not supported
s.remove(30)
print(s)

f=frozenset(s)
g = f.copy()
print(g)
#f.remove(20) # frozen set does not supported update,remove

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print ( A | B) #UNION

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print ( A & B ) # Intersection

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B) #Difference

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A ^ B) # Symmetric Difference:



