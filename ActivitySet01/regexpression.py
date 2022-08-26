from ast import pattern
from collections import abc
import re
txt="The rain in Spain is fun"
x=re.search("^The.*fun$",txt)
print(x)
print(x.start())
print(x.end())
print("matched word will display",x.group())
print("start,end index",x.span())
a=re.match("^The.*fun$",txt)#matched word will display
m=re.findall("[a-m]",txt)#find all the lowercase betweeen a to m

print(m)
print(a)
if x:
    print("pattern found inside the txt")
else:
    print("pattern not found")
z="abce"
pattern1='..'
c=re.match(pattern1,z)
p="abyss"
pattern2='^a...s$'
w=re.match(pattern1,p)
print(w)
print(c)
input='aaa'
v=re.sub('a','b',input,2)#a get replaced by b
print(v)
d=re.subn('a','b','abaa')#prints number of changes
print(d)
s1=re.findall('a','ababa')
print(s1)
inp="am i cute"
i1=re.findall('^a',inp)
print(i1)
g=re.split('a','aababa',3)
print(g)
g1=re.split('a','aabababa',3)
print(g1)
pattern3='\w+'#alphanumeric
s5='shiva'
s4=re.search(pattern3,s5)
print(s4)