def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap

year = int(input("请输入一个年度："))
if year < 1900 or year > 10**5:
    print("you input year is error number")
else:
    print(is_leap(year))