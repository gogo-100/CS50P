expression = input("Expression: ")
x, y, z = expression.split(" ")
print(y)
if y == '+' :
    print(f"{int(x) + int(z):.1f}")
elif y == '-':
    print(f"{int(x) - int(z):.1f}")
elif y == '*':
    print(f"{int(x) * int(z):.1f}")
else:
    print(f"{int(x) / int(z):.1f}")