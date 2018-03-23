# 错误1，用列的方式来思考是错误的
# for j in range(1,10):
#     for i in range(1,10):
#         if (i >= j):
#             print(i,"*",j,"=",i*j)

# 1. 横向看计算机的输出方式；2.如何打印出2*1,2*2的方式 表达；3.i的值决定了j的循环方式；4.i打印完就会换行；5.同时解决print 换行问题
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end='\t')
    print('\r')

# 解决取消print 回车问题
# for i in range(1,5):
#     print(i,end=' ')