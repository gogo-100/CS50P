
names = []

while True:
    try:
        str = input("Name: ")
    except:
        break
    else:
        names.append(str)

if len(names) > 0:
    print(f"Adieu, adieu, to {names[0]}", end = "")
    for i in range(1,len(names)):
        if len(names) == 2:
            print(f" and {names[i]}", end = "")
        elif i == len(names)-1:
            print(f", and {names[i]}", end = "")
        else:
            print(f", {names[i]}", end = "")

