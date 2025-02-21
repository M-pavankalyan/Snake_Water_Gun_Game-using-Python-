import random
print("key:- s:snake w:water g:gun")
youstr = input("chosse your key:")  #Getting input from user.
computer = random.choice([1,-1,0])  #Getting input from computer.
youdisc = {"s":1,"w":-1,"g":0}
reverse_disc = {1:"snake",-1:"water",0:"gun"}
you = youdisc[youstr]             
print(f"\n you choosed {reverse_disc[you]} \n computer chossed {reverse_disc[computer]}")
if(you == computer):
    print("Draw Match!")
else:
    if(computer == 1 and you == 0):
        print("\n You Won!")
    elif(computer == -1 and you == 1):
        print("\n You Won!")
    elif(computer == 0 and you == -1):
        print("\n You Won!")
    elif(computer == 1 and you == -1):
        print("\n You lose!")
    elif(computer == -1 and you == 0):
        print("\n You lose!")
    elif(computer == 0 and you == -1):
        print("\n You lose!")
