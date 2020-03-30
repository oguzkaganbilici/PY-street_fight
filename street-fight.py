import random,os,time

class Enemy():
    def __init__(self):
        self.power = random.randint(5,20)
        self.health = random.randint(10,100)
        self.shield =random.randint(10,100)

    def hit(self):
        damage = self.power - Player.shield
        Player.health -= damage


class Player():
    def __init__(self,name,character):
        self.name =name
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
            self.shield = 70
        elif self.charecter == "3":
            self.charecter = "Archer"
            self.power = 180
            self.health = 75
            self.shield = 100
        elif self.charecter == "4":
            self.charecter = "Supporter"
            self.power = 100
            self.health = 100
            self.shield = 200


    def hit(self,enemy):
        damage = self.power - enemy.shield
        enemy.health -= damage
        if enemy.health <=0:
            print("Enemy was killed!!")
            enemies.remove(enemy)
            input()
        else:
            print("Oh no! He is still alive! Hit again..")
            input()

def seeenemies():
    for i in enemies:
        print("{}.Enemy:| Health:{} | Shield:{} | Power:{} |".format(enemies.index(i),i.health,i.shield,i.power))

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


    player = Player(name, char)
    print("Hero's Name: {}, Character: {}, Health: {}, Shield: {}, Power: {}".format(player.name, player.charecter,
                                                                                     player.health, player.shield,
                                                                                     player.power))
    print("Created! press enter for fight!")
    input()


    os.system("clear")

    print("Enemies are coming...! Be quick..")
    time.sleep(1)
    for i in enemies:
        print("{}.Enemy:| Health:{} | Shield:{} | Power: {} |".format(enemies.index(i), i.health, i.shield, i.power))
        time.sleep(0.1)
    control = True

    try:
        pick_enemy = int(input("Pick a enemy for attack:"))
        attack = enemies[pick_enemy]
        player.hit(attack)
        control = False
    except ValueError:
        print("Please pick a enemy!")



    if control == False:
        for a in range(len(enemies),0,-1):
            print(a,"Round")
            if a == 0:
                print("Congrat.....")
            else:
                print("Continue to fight")
                pick_enemy = int(input("Pick a enemy for attack:"))
                attack = enemies[pick_enemy]
                player.hit(attack)


            seeenemies()
            input()

    """
    print("""
    """Welcome
    press 1 for see enemies
    press 2 for create your hero and fight!
    
    ) 
    secim = input("Seciminiz:")

    if secim == "1":
        for i in enemies:
            print("Enemy {}:| Health {} | Shield {} | Power {} | ".format(enemies.index(i)+1, i.health, i.shield,i.power))
        input()
        

"""



