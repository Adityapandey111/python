
import random

def decide(user,comp):
    
    if user==comp:
        return 'Its a tie!'
    elif (user=='s' and comp=='w') or (user=='w' and comp=='g') or (user=='g' and comp=='s'):
        return "You win!"
    return "You Lose"

print('\n')
print('<-----------------------Welcome to the game----------------------->')

ls=['w','s','g']
dict={'s':'Snake', 'w':"Water", 'g':"Gun"}

while(True):
    user=input('Enter your (w)ater or (s)nake or (g)un : ').lower()
    computer=random.choice(ls)

    print('\n')
    print(f"You chose {dict[user]} and Computer chose {dict[computer]}")
    print("\n")

    print('<----------------result----------------->')
    print('\n')
    print(decide(user,computer))
    print('\n')
    print('<--------------------------------------->')
    ch=input('Press 0 to play further : ')
    if ch!='0':
        break
    print('\n')