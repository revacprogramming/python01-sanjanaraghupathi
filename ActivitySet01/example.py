from ctypes import Union


L1=[4,2,6]
s1={1,2,3}
print(L1)
print(s1,type(s1))
print(type(L1))
s2=set(L1)
print("s2=",s2,type(s2))
#print(s2[0]) no method of indexing in set
S=set(range(1,6))
print(S)
s1.add(10)#only one argument using add
s1.update({10,34,56,23})#multiple data element insertion
print(s1)
s1.update([10,40,9])
print('s1=',s1)
p=s1.union(s2)#also can use |
print(p)
print(s1.pop())#remove random element
s1.remove(40)#delete particular element,show error if element is not there in set
s1.discard(40)#even if number is not there in set no error will be displayed

print(len(s1))
for i in s1:
    print(i)
print('a' in s1)
s3=s1
print('s3',s3)
s3.discard(34)
print(s1)
s4=s1.copy()
print('s4=',s4)
s4.remove(10)
print('s1=',s1)
print('s4=',s4)
d=s1.intersection(s2)
a=(s1&s2)#same as intersection
print(a)
print(d)
f=s1.difference(s2)#also can use -,left out element in s1 is displayed
print(f)
m=s1.symmetric_difference(s2)#left out element in s1 and s2 is displayed
print(m)
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1>=s2)
