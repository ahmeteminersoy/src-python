import random
liste = ["Taş", "Kağıt", "Makas"]
idx = 0
comp = 0
user = 0
while True:
    if(user == 2 or comp == 2):
        break
    userchoice = input("Taş, Kağıt, Makas!! :").capitalize()
    computerselect = random.choice(liste)
    if (computerselect == userchoice):
        print("Berabere")
        print(userchoice, computerselect)
        continue
    if (computerselect == "Taş" and userchoice == "Makas" or computerselect == "Kağıt" and userchoice == "Taş" or computerselect == "Makas" and userchoice == "Kağıt"):
        comp += 1
        print("Bilgisayar kazandı", userchoice, computerselect, sep=",")
        idx += 1
        continue
    if (computerselect == "Makas" and userchoice == "Taş" or computerselect == "Taş" and userchoice == "Kağıt" or computerselect == "Kağıt" and userchoice == "Makas"):
        user += 1
        print("Sen kazandın", userchoice, computerselect, sep= ",")
        idx += 1
        continue
if(comp > user):
    print("Bilgisayar kazandı", user, comp, sep=",")
else:
    print("Sen kazandın", user, comp, sep= ",")

