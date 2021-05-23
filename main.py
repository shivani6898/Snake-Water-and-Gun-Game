import random
# Snake Water Gun Game
def Gamewin(comp,you):
    if (comp == you):
        return None
    elif (comp == 's'):
        if (you == 'w'):
            return False
        else:
            return True
    elif (comp == 'w'):
        if(you == 's'):
            return True
        else:
            return False
    elif (comp == 'g'):
        if (you == 's'):
            return False
        else:
            return True

print("Computer turn : snake(s),water(w) & gun(g)?")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'
you = input("Player turn : snake(s),water (w) & gun(g)?")
a = Gamewin(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if a == None:
    print("tie")
elif a:
    print("You Win")
else:
    print("YOu Lose")