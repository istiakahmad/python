lst=[10,20,'Bharath',-10,30.5]
print(lst)
print(lst[3])
print(lst[3:5]) # from 3 to 5-1=4
print(lst*4) # 4 time  print
print(len(lst))

lst.append(40)
lst.remove('Bharath')
del(lst[1])
print(lst)

#lst.clear() # clear the list
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 99)
print(lst)

lst.sort(reverse=True)
print(lst)

lst.sort(reverse=False)
print(lst)

