#思路：计算长度，除以k
#将字符切片，从0开始
#判断切片完的字符是否有重复字母
#去除重复的字母，最后打印出来
#zip(*[iter(S)]*N)是将原有字符按照N进行划分
#10实现了对part进行去重，最后打印出来
S,N = input(),int(input())
for part in zip(*[iter(S)]*N):
    d = dict()
    print(''.join([d.setdefault(c,c) for c in part if c not in d]))




