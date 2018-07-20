import time
import random

areas_been = []
life = 10
energy = 10
skill = 1
enemy_health = None
fight_status = "yes"
normal_enemies = ["a wild gang member", "a drunkard", "the school bully", "a wild dog", "a delusional Justin Beiber fan"]
hard_enemies = ["a furious Mum", "a furious Dad"]
damage = skill + 4

enemy_health = 10
enemy_number = random.randint(0,5)
enemy = normal_enemies[enemy_number]
print("You have encountered",enemy,"\n")
time.sleep(2)

def normal_fight():

    while fight_status == "yes":

        if life <= 0 or energy <= 0:

            print("GAME OVER....")
            time.sleep(2)
            quit()

        print("Life =",life)
        print("Energy =",energy)
        print("Skill =", skill)
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
                    
                    print("Life =",life)
                    print("Energy =",energy)
                    print("Skill =", skill)

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

