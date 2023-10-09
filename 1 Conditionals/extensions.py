str = input("File name: ").lower().strip()
str = str[str.rfind("."):]

match str:
    case ".gif":
        print("image/gif")
    case ".png":
        print("image/png")
    case ".txt":
        print("text/plain")
    case ".jpg" | ".jpeg" :
        print("image/jpeg")
    case ".pdf":
        print("application/pdf")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")