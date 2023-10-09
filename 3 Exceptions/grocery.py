
gdict = {}

while True:
    try:
        str = input().upper().strip()
    except EOFError:
        break
    if str in gdict:
        gdict[str] += 1
    else:
        gdict[str] = 1

for key in sorted(gdict):
    print(gdict[key],key,sep=" ")
