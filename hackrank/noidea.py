#Ë¼Â·£º½«setA,setB ÊäÈëµÄÖµµ½arryÖĞ½øĞĞÅĞ¶ÏÈç¹ûÓĞÔò¼Ó1È»ò -1

n,m = input().split()
arr = input().split()
setA = set(input().split())
setB = set(input().split())
print(sum([ (i in setA) - (i in setB) for i in arr]))
£
