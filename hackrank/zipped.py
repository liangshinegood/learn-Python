#思路：每一门科目所有学生的成绩是一个列表
#用zip,计算所有学生的成绩

a,y = map(int,input().split())
scores = [map(float,input().split()) for _ in range(y)]
[print(sum(student)/y) for student in zip(*scores)]





