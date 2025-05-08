import random

rand=random.randint(1,100)

user=int(input("Enter a number between 1 to 100 : "))
cnt=1
while(rand!=user):
    cnt+=1
    if(rand>user):
        # print()
        user=int(input("Enter Higher number please : "))
    elif(rand<user):
        user=int(input("Enter Lower number please : "))

print(f"You guess the right number {rand} in {cnt} guesses!")