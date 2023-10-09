def main():
    str = input("Input: ")
    sh = short(str)
    print(sh, end="")

def shorten(word):
    for ch in 'aeiouAEIOU':
        word = word.replace(ch,"")
    return word

if __name__ == "__main__":
    main()