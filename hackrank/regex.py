#ÕÊ×ÏÈÒªÁË½âÕıÔò±í´ïÊ½µÄË¼Ïë
# ¸ù¾İ¹æÔò½øĞĞÅĞ¶Ï
# re ÊÇÕıÔò±í´ïÊ½µÄÄ£¿é
# re.compile ÊÇ½«×Ö·û´®ĞÎÊ½µÄÕıÔò±í´ïÊ½±àÒëÎªpattern¶ÔÏó
import re
for _ in range(int(input())):
    isreg = True
    try:
        reg = re.compile(input())
    except re.error:
        isreg = False
    print(isreg)
