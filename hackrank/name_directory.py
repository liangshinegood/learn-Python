# ˼·��1. ������������2.���ͬ������������˳������3.�����M ��ʽΪMr.
# �����F ��ʽΪMs.

def person_lister(f):
    def inner(people):
        return map(f,sorted(people,key=lambda x:x[2]))
    return inner




