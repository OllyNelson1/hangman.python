import time
import random

areas_been = []
life = 10
energy = 10
skill = 1
enemy_health = None
fight_status = "no"
normal_enemies = ["a wild gang member", "a drunkard", "the school bully", "a wild dog", "a delusional Justin Beiber fan"]
hard_enemies = ["a furious Mum", "a furious Dad"]
damage = skill + 4

def stats(life, energy, skill):
    print("Life =",life)
    print("Energy =",energy)
    print("Skill =", skill)

def normal_fight():

    enemy_health = 10
    enemy_number = random.randint(0,5)
    enemy = normal_enemies[enemy_number]
    print("You have encountered",enemy,"\n")
    time.sleep(2)

    while fight_status == "yes":

        if life <= 0 or energy <= 0:

            print("GAME OVER....")
            time.sleep(2)
            quit()

        stats(life, energy, skill)
        print("Enemy health", enemy_health)

        damage = skill + 4

        time.sleep(2)
        
        action = input("\nDo you want to attack or run away? >>")

        if action == "attack":

            time.sleep(2)

            print("*Energy - 1*")
            energy = energy - 1
            success = random.randint(1,10)

            if success == 1 or success == 2 or success == 3 or success == 4 or success == 5 or success == 6 or success == 7:
                time.sleep(2)
                print("You succssfully hit for",damage,"health!")
                enemy_health = enemy_health - damage
                time.sleep(1)      

                if enemy_health <= 0:

                    time.sleep(2)
                    print("You successfully killed your enemy!!!")
                    print("Skill + 1!")
                    skill = skill + 1 
                    
                    time.sleep(2)
                    
                    stats(life, energy, skill)

                    fight_status = "no"
                    break

                else:
                    time.sleep(2)
                    print("The enemy hit for 2 health!!!\n")
                    life = life - 2

            else:
                time.sleep(2)
                print("You missed, lose 1 more energy!!!")
                energy = energy - 1
                time.sleep(2)
                print("The enemy hit for 2 health!!!")
                life = life - 2
            

        elif action == "run away":

            success = random.randint(1,10)

            if success == 1 or success == 2 or success == 3:

                time.sleep(2)
                print("You successfully escaped! Lose 3 energy!")
                energy = energy - 3
                fight_status = "no"
                break
                
            else:

                time.sleep(2)
                print("You didn't escape, they were too fast!")
                time.sleep(2)
                print("GAME OVER....")
                quit()


print("Welcome to my Text-Based Adventure Game!")
time.sleep(1)
name = input("What is your name? >>")
time.sleep(2)
print("Hello",name)
time.sleep(1)

print("~~~~~~~~~~~~~~~~~~~~")
time.sleep(1)
print("*you are at school and you realised you left your P.E kit at home*")
time.sleep(4)
print("*you need to find your way home safely and get your P.E kit\nor you'll face punishment when you return to school*")
time.sleep(5)
direction = input("\nSelect the direction you want to take:\nNorth\nSouth\nEast\nWest\n>>")
area = "school"
areas_been.append(area)

if direction == "North":
    area = "forest"
    areas_been.append(area)
    random_number = random.randint(1,10)
    print("*you have arrived at the scary forest...*")
    time.sleep(1)
    
elif direction == "South":
    area = "bridge"
    areas_been.append(area)
    random_number = random.randint(1,10)
    print("*you have arrived at the shaky bridge...*")
    
elif direction == "East":
    area = "hill"
    areas_been.append(area)
    random_number = random.randint(1,10)
    print("*you have arrived at the steep hill...*")
    

elif direction == "West":
    area = "beach"
    areas_been.append(area)
    random_number = random.randint(1,10)
    print("*you have arrived at the baron beach...*")


if random_number == 2 or random_number == 4 or random_number == 6 or random_number == 8 or random_number == 10:
    fight = "yes"
    fight_status = "yes"
    normal_fight()
    time.sleep(2)

else:
    fight = "no"
    time.sleep(1)
    print("You made it through safely!!!")

time.sleep(1)
stats(life, energy, skill)



    

















