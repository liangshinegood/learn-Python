#�����Ҫ�˽�������ʽ��˼��
# ���ݹ�������ж�
# re ��������ʽ��ģ��
# re.compile �ǽ��ַ�����ʽ��������ʽ����Ϊpattern����
import re
for _ in range(int(input())):
    isreg = True
    try:
        reg = re.compile(input())
    except re.error:
        isreg = False
    print(isreg)
