'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
step2=0
step3=0
step4=0
step5=0
step6=0
hello = input ("what is your characters name: ") 
print ("hello " + hello + " you are here to save the world as it is overun with monsters")
answer=input("A.go to sleep B.start fighting: ")
next
if answer=="A":print("you died in your sleep")
if answer=="B":step2=input("you decided to fight will you A.start with slimes or B.fight the final boss: ")
next
if step2=="B":print("he killed you immediatley")

if step2=="A":step3=input("you beat them up and got their slime do you want to A. sell it or B. eat it: " )
next
if step3=="B":print("*_* it was a poison slime you died")
if step3=="A":step4=input("you got some money do you A.buy a sword or B.buy some armor: ")
next
if step4=="A":print("you fell on the sword...wait what did you kill the slimes with")
if step4=="B":step5=input("nice armor but you are hungry do you A.go to the soup shop and spend all your money or B.go to the cracker store and have $5 left: ")
next
if step5=="A":print("you had good meal but when you left you got attacked they didnt believe you were out of money and killed you:(")
if step5=="B":step6=input("you don't feel full and regret your choice until you get attacked do you A.fight them or B.give up youre money: ")
next
if step6=="B":print("you give up your 5 dollars and they stab you...X-X")

