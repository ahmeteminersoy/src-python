def isPalindrom(str):
    if str == str[::-1]:
        return True
    else:
        return False
while True:
    str = input("Bir yazi giriniz:")
    if str == "quit":
        print("Goodbye..!")
        break
    if isPalindrom(str):
        print(str, "yazısı palindromdur")
        
    else:
        print(str, "yazısı palindrom değildir")
