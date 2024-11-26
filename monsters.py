class Mon:
    def __init__(self, level, name, health, attack, defence):
        self.name = name
        
        self.max_health = health
        self.health = health

        self.attack = attack
        self.defence = defence

        self.moves = list()
        self.mymoves = list()

    def deal_damage(self, other):

        other.take_damage(self)

    def take_damage(self,other):
        print(other.name+" dealt "+str(other.calculate_damage(self))+" to "+self.name+"!")
        self.health -= other.calculate_damage(self)

    def calculate_damage(self,other):
        return self.attack-other.defence

    def health_bar(self):
        div = self.max_health/100
        percent = int(((self.health/self.max_health)*100)/5)
        full_bar = int((self.max_health/div)/5)
        return (full_bar*"=")+"\n"+(percent*"|")+"\n"+(full_bar*"=")

    def attack1(self):
        pass

    def __str__(self):
        return "Name: "+self.name+"\n"+self.health_bar()+"\nHealth: " +str(self.health)+"/"+str(self.max_health)

class JollyRancher(Mon):
    def __init__(self, level, name="Jolly Rancher", health=100, attack=20, defence=5):
        self.name = name
        
        self.max_health = health
        self.health = health

        self.attack = attack
        self.defence = defence

    def attack1(self,other):
        self.deal_damage(other)
