def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)> 6 or len(s)<2:
        return False
    if not s.isalnum():
        return False
    if (not s[0].isalpha()) or (not s[1].isalpha()):
        return False
    flag = False
    for ch in s:
        if flag:
            if ch.isalpha():
                return False
        elif ch.isnumeric():
            flag = True
            if ch == '0':
                return False
    return True
main()