#˼·����setA,setB �����ֵ��arry�н����ж���������1Ȼ� -1

n,m = input().split()
arr = input().split()
setA = set(input().split())
setB = set(input().split())
print(sum([ (i in setA) - (i in setB) for i in arr]))
�
