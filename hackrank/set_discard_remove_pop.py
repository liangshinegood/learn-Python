#˼·�������ǵ�������10�β���ʱ����Ҫ����10�β���
#���������ݺ󣬽����������ʱ��������Ĳ�������Ӧ������ν��Ӧ����֮ǰ��˼·�Ѿ�OK��
#s.{0}({1}) ͨ����ʽ���ķ�ʽ���б��ʽ���ѣ���s.remove(9)
#*input().split ��ȡ������Ԫ�ص�ֵ

n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))



