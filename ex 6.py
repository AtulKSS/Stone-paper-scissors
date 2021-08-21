print("stone paper scissors game")

print("CHOOSE YOUR OPTION")

ele=("stone"),("paper"),("scissor")
chance=0

s="stone"
p="paper"
K="scissors"
rada=(s,p,K)

import random
cham=random.choice(rada)
user=int(input("1 for Stone\n""2 for Paper\n""3 for Scissros"))
rule= 4


while True:


    if user == 1:
        print("my choice is", cham)
        if cham==p:
            print("u loose")
        elif cham==s:
            print("TIE")
        elif cham==K:
            print("u win")
        if rule==4:
            rule=int(input("Press 4 to continue"))
        user = int(input("1 for Stone\n""2 for Paper\n""3 for Scissros"))
        continue



    elif user==2:
        print("My choice is",cham)
        if cham==s:
            print("u win")
        elif cham==p:
            print("TIE")
        else:
            print("u loose")
        if rule==4:
            rule=int(input("Press 4 to continue"))
        user = int(input(" 1 for Stone\n""2 for Paper\n""3 for Scissros"))
        continue


    elif user==3:
        print("My choice is",cham)
        if cham==s:
            print("u loose")
        elif cham==K:
            print("TIE")
        else:
            print("U win")
        if rule == 10:
            print("radarada")

        rule = int(input("Press 10 to Exit"))
        break

































