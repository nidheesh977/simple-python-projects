a = [1,2,3,4,5]
b = a
c=[]
for i in a:
    c.append(i)

print('a -', a)
print('b -', b)
print('c -', c)
print(id(a))
print(id(b))
print(id(c))