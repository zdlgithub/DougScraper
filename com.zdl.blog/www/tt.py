import os


aa=['a','b','c','d']
aa.insert(1,'e')
print(aa)

i=1

print('abc\ndddd')

split_char = '' if i==1 else ','
print(split_char)

ta = ['a','b','c','d']
aindex = ta.index('e') if 'e' in ta  else -1
print('aindex:',aindex)
stra = ';'.join(ta)
print(stra)
tas = stra.split(';')
print(tas)

print('hello pyton')

abspath=os.path.abspath(__file__)
print(abspath)
print(os.path.dirname(abspath))
print(os.path.dirname(os.path.dirname(abspath)))
print(os.path.join(os.path.dirname(os.path.dirname(abspath)),'library','abc.csv'))

import collections 

akey='a1'
avalue='my a1'
bkey='b1'
bvalue='my b1'

mydict ={}
mydict[akey]=avalue
mydict[bkey]=bvalue

for k in mydict:
	print('mydict[%s]:' % k,mydict[k])
	
