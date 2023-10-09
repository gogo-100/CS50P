months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    d = input("Date: ").strip()
    if d.find(",") != -1:
        mm,dd,yy = d.split()
        dd = dd[:-1]
        try:
            mm = months.index(mm) + 1
        except:
            continue
    elif d.find("/") != -1:
        mm,dd,yy = d.split("/")
    try:
        if int(mm) <= 12 and int(dd) <= 31:
            break
    except:
        continue

print(f"{yy}-{mm:0>2}-{dd:0>2}", end="")
