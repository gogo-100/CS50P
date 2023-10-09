str = input("Greeting: ").lower().strip()


if str[:5]=="hello":
    print("$0")
elif str[0]=='h':
    print("$20")
else:
    print("$100")