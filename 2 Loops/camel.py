str = input("camelCase: ")

res = []
last = 0

for i in range(1,len(str)):
    if str[i].isupper():
        res.append(str[last:i].lower())
        last = i
res.append(str[last:].lower())
print('_'.join(res))