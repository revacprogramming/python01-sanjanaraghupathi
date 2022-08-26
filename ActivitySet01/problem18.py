#email
import re
pattern='(\w)+@(\w+\.)+(com)'
email='jphn_123@gmail.com'
s1=re.search(pattern,email)
if s1:
    print('search is successful')
else:
    print('unsuccessful')

#phone number
import re
pattern='(0|91)?[6-9][0-9]{9}'
p1='9901441075'
s1=re.search(pattern,p1)
if s1:
    print('search is successful')
else:
    print('unsuccessful')


import re
pattern='^a...z$'
word=input('enter a word')
s1=re.match(pattern,word)
if s1:
    print('search is successful')
else:
    print('unsuccessful')


