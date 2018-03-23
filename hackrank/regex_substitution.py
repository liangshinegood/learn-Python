import re
n = int(input())

for i in range(n):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )',lambda x:'and' if x.group() == '&&' else 'or',input()))


