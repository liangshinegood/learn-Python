#导入nametuple
# namedtuple('classsheet','id  marks name class')
# student = classsheet(id = xxx,marks =xxx,name=xxx,class=xx)
# student.id , student.mark,student.name,student.class
# average = student.mark/totalstudent  用循环算出sum student.mark
#print average
# 如果不超过四行解决的话：
# 第一行：输入值处理（难点在于怎样连续的输入，并储存起来）
# 第二行：计算sum student.mark,并算出average
# 第三行：输出
# from collections import namedtuple #不需要用它的这个方法
stu, marks = int(input("请输入学生数量：")), input("学生信息：").split().index("MARKS")
print (sum([int(input().split()[marks]) for _ in range(stu)]) / stu)

