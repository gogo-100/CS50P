
while True:
    try:
        a,b = input("Fraction: ").split("/")
        x = round(int(a) / int(b) *100)
        if int(a) > int(b):
            continue
    except:
        pass
    else:
        if x <= 1:
            print("E")
        elif x >= 99:
            print("F")
        else:
            print(f"{x}%")
        break
