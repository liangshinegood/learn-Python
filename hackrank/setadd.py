# 这道题的思路：本质上就是用set方法排重，然后求和

print(len(set([str(input())for x in range(int(input()))])))
