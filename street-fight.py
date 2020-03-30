import random,os,time
os.system("clear")


class Enemy():
    def __init__(self):
        self.power = random.randint(150,200)
        self.health = random.randint(10,100)
        self.shield = random.randint(10,100)

    def hitt(self, enemy):
        damage = self.power - enemy.shield
        if damage >= 0:
            enemy.health -= damage
            if enemy.health <= 0:
                os.system("clear")
                print("Game Over, YOU DIED BRO!")
                input("press enter for quit")
            else:
                pass
        else:
            damage = 0
            enemy.health -= damage


class Player():
    def __init__(self, name, character):
        self.name = name
        self.charecter = character
        if self.charecter == "1":
            self.charecter = "Warrior"
            self.power = 150
            self.health = 80
            self.shield = 150

        elif self.charecter == "2":
            self.charecter = "Sorcerer"
            self.power = 200
            self.health = 50
            self.shield = 900
        elif self.charecter == "3":
            self.charecter = "Archer"
            self.power = 180
            self.health = 75
            self.shield = 120
        elif self.charecter == "4":
            self.charecter = "Supporter"
            self.power = 100
            self.health = 100
            self.shield = 200

    def hit(self,enemy):
        damage = self.power - enemy.shield
        enemy.health -= damage
        if enemy.health <= 0:
            print("Enemy was killed!!")
            enemies.remove(enemy)
            input("Enter for continue to fight")
        else:
            print("Oh no! He is still alive! Hit again..")
            input("Enter for continue to fight")


def seeenemies():
    for i in enemies:
        print("{}.Enemy:| Health:{} | Shield:{} | Power:{} |".format(enemies.index(i)+1,i.health,i.shield,i.power))

enemies = list()

for i in range(1,11):
    enemies.append(Enemy())


while True:
    os.system("clear")
    name = input("Write your hero's name:")
    char = input("""
            Choose your Character:
            [1]Warrior
            [2]Sorcerer
            [3]Archer
            [4]Supporter
            :""")

    player = Player(name,char)
    print("Hero's Name: {}, Character: {}, Health: {}, Shield: {}, Power: {}".format(player.name, player.charecter,
                                                                                     player.health, player.shield,
                                                                                     player.power))
    print("Created! press enter for fight!")
    input()

    os.system("clear")
    check = True
    print("Enemies are coming...! Be quick..")
    time.sleep(1)
    for i in enemies:
        print("{}.Enemy:| Health:{} | Shield:{} | Power: {} |".format(enemies.index(i)+1, i.health, i.shield, i.power))
        time.sleep(0.1)
    control = True
    enemy_attack = enemies[random.randint(1,len(enemies)-1)]
    enemy_attack.hitt(player)
    print("YOUR HEALTH: {}".format(player.health))
    while control:
        try:
            pick_enemy = int(input("Pick a enemy for attack:"))
            attack = enemies[pick_enemy -1]
            player.hit(attack)
            enemy_attack.hitt(player)
            print("YOUR HEALTH: {}".format(player.health))
            if player.health == 0:
                os.system("clear")
                print("Game Over, YOU DIED BRO!")
                input("press enter for quit")
            else:
                control = False
        except:
            if player.health == 0:
                os.system("clear")
                print("Game Over, YOU DIED BRO!")
                input("press enter for quit")
            else:
                print("Please pick a enemy:")

    if control == False:
        for a in range(len(enemies),0,-1):
            print("------------- Round {} -------------".format(a))
            os.system("clear")
            seeenemies()
            print("YOUR HEALTH: {}".format(player.health))

            try:
                pick_enemy = int(input("Pick a enemy for attack:"))
                attack = enemies[pick_enemy -1]
                player.hit(attack)
                enemy_attack.hitt(player)
                if player.health == 0:
                    os.system("clear")
                    print("Game Over, YOU DIED BRO!")
                    input("press enter for quit")
                    exit()
                else:
                    print("Please pick a enemy:")
            except:
                if len(enemies) == 0 or player.health == 0:
                    print("Congralations.. ALL ENEMIES ARE DIED")
                    print("Press enter for quittt")
                    quit()
                else:
                    print("please pick a enemy:")

