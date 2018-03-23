listPhysics = []
for _ in range(int(input("请输入学生的个数："))):
    nameScore = []
    name = input("请输入学生的姓名：")
    score = float(input("请输入学生的分数："))
    nameScore.append(name)
    nameScore.append(score)
    listPhysics.append(nameScore)
listScore = []
for a in listPhysics:
    listScore.append(a[1])
setScore = set(listScore)
listScore = sorted(setScore)
lowestSecond = listScore[1]
lowestSecondStudent=[]
for b in listPhysics:
    if b[1] ==lowestSecond:
        lowestSecondStudent.append(b[0])
lowestSecondStudent.sort()
for name in lowestSecondStudent:
    print(name)

