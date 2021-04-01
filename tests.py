import random

#value = random.randint(1,10)
#print(value)
#0.2
print('   Colossal Cave')
print('The First Advanture')
name = input('What is your name?')
role = input('What is your role? [wizard,warrior,monk,mage]')
age = int(input('What is your age?'))
print('Hi',name,'Your role is',role)
if age >20:
    print('You are old')
else:
    print('You are quite young')
playerHealth = random.randint(50,100)
monsterHealth = random.randint(50,100)
#if pH < mH print(danger) if pH = mH print(you will make it) else print(sure win)

print('Player Health:',playerHealth)
print('Monster Health:',monsterHealth)
if playerHealth < monsterHealth:
    print('Danger')
elif playerHealth == monsterHealth:
    print('You will make it')
else:
    print('Sure win')

monsters=['Zombie','Shark','Piranha']
for monster in monsters:
    print(monster)

#[nilai monster health]
#[monster is bleeding : health]
mHealths = [60,50,40,30]
for x in mHealths:

    print('Monster is bleeding:',str(x))

if monsterHealth%age > 5 & playerHealth <65:
    print('You got chances to get gold')
elif monsterHealth%age >3 & playerHealth <40:
    print('You got coin instead')
else:
    print('No treasure for you')
