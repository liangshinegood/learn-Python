dictA = {'A':3,'a':1,'L':'d'}
dictC = {4,5,6,7}
listA = [12,13,14]
print('the dicA key is :',dictA.keys())
print('the dicA value is:',dictA.values())
print('the items is :',dictA.items())
print('the fromkey is 1:',dictA.fromkeys('b'))
print('the fromkey is 2:',dictA.fromkeys('a'))
print('the fromkey is 3:',dictA.fromkeys(dictA))
print('the fromkey is 4:',dictA.fromkeys(dictA,dictC))
print('the fromkey is 5:',dictA.fromkeys(dictA,listA))
print('the get is 1:',dictA.get('l'))
print('the get is 2:',dictA.get('L'))
dictB = dictA.copy()
print('use the copy and the dicB is ',dictB)

theStr = dictA.setdefault('L')
print('setdefault method is 1 :',theStr)
theStr1 = dictA.setdefault('w')
print('setdefault method is 1 :',theStr1)
print('the new dictA is:',dictA)
dictA.update(w = '5')
print('the update dictA is 1:',dictA)
r3 = {'t':90}
dictA.update(r3)
print('the update dictA is 2:',dictA)