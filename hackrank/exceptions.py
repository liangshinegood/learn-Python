#����ʽ���ص�˼�룺
#����������룬range(input��ʽ)
#��map��ӳ�䣬�������ֵת��Ϊint
for i in range(int(input())):
    try:
        a,b = map(int,input().split())
        print(a/b)
    except BaseException as e:
        print("Error Code:",e)


