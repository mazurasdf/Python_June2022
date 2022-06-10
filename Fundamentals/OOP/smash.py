class Fighter:
    def __init__(self, name, style, weight, speed, strength, player_num):
        #name, fighting style, weight, speed, strength, player_num
        print("parent constructor here!")
        self.name = name
        self.style = style
        self.weight = weight
        self.speed = speed
        self.strength = strength
        self.player_num = player_num
        self.percentage = 0
    
    def attack(self,opponent):
        damage = 7
        opponent.percentage += damage
        print(f"{self.name} attacks {opponent.name} and deals {damage}%!!!!!!")

    def special(self,opponent):
        damage = 15
        opponent.percentage += damage
        print(f"{self.name} performs a special on {opponent.name} and deals {damage}%!!!!!!")

    def print_stats(self):
        print(f"Stats for {self.name}")
        print(f"style: {self.style}")
        print(f"weight: {self.weight}")
        print(f"speed: {self.speed}")
        print(f"strength: {self.strength}")
        print(f"player_num: {self.player_num}")
        print(f"percentage: {self.percentage}")

peach = Fighter("Peach","zoner", 5,5,6,1)
# falcon = Fighter("Captain Falcon", "rushdown", 6, 8, 7, 2)
# falcon.print_stats()
# peach.special(falcon)
# falcon.print_stats()

class Pikachu(Fighter):
    def __init__(self,player_num):
        super().__init__("Pikachu", "electric", 3, 7, 6,player_num)
    def special(self,opponent):
        damage = 7

        for i in range(0,3):
            opponent.percentage += damage
            print(f"{self.name} quick attacks {opponent.name} and deals {damage}%!!!!!!")
class Samus(Fighter):
    def __init__(self,player_num):
        super().__init__("Samus", "zoner",8,4,7,player_num)
        self.charged = False
    def special(self,opponent):
        if(self.charged):
            self.charged = False
            damage = 35
            opponent.percentage += damage
            print(f"{self.name} fires her laser at {opponent.name} and deals {damage}%!!!!!!")
        else:
            self.charged = True
            print(f"{self.name} is charging her arm cannon!")

pika = Pikachu(1)
pika.print_stats()
# pika.special(peach)
samus = Samus(2)
samus.special(pika)
pika.print_stats()
samus.special(pika)
pika.print_stats()