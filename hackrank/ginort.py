#思路：列好所有的可能然后排序
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(),key = order.index),sep='')



