def isPalindrom(s, *, ignorecase = False):
    if ignorecase:
        s = s.upper()
    print(s)

    if s == s[::-1]:
        return True
    else:
        return False
if __name__ == '__main__':  
    while True:
        str = input("Bir yazi giriniz:")
        if str == "quit":
            print("Goodbye..!")
            break
        if isPalindrom(str, ignorecase=True):
            print(str, "yazısı palindromdur")
            
        else:
            print(str, "yazısı palindrom değildir")


