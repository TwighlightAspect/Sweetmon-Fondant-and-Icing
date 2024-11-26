import random as rn

class Mon:
    def __init__(self, level, name, health, attack, defence):
        self.name = name
        
        self.max_health = health
        self.health = health

        self.attack = attack
        self.defence = defence

        self.moves = list()
        self.mymoves = list()
        
        self.level = level
        
        self.stats = [self.max_health,self.attack,self.defence,self.moves]

    def deal_damage(self, other):

        other.take_damage(self)

    def take_damage(self,other):
        print(other.name+" dealt "+str(other.calculate_damage(self))+" damage to "+self.name+"!")
        self.health -= other.calculate_damage(self)

    def calculate_damage(self,other):
        return self.attack-other.defence

    def health_bar(self):
        div = self.max_health/100
        percent = int(((self.health/self.max_health)*100)/5)
        full_bar = int((self.max_health/div)/5)
        return (full_bar*"=")+"\n"+(percent*"|")+"\n"+(full_bar*"=")
    
    def all_stats(self):
        pass

    def attack1(self):
        pass

    def __str__(self):
        return "Name: "+self.name+" lvl."+str(self.level)+"\n"+self.health_bar()+"\nHealth: " +str(self.health)+"/"+str(self.max_health)

class JollyRancher(Mon):
    def __init__(self, level, name="Jolly Rancher", health=rn.randint(18,20), attack=rn.randint(5,7), defence=rn.randint(2,3)):
        self.name = name
        
        self.max_health = health
        self.health = health

        self.attack = attack
        self.defence = defence
        
        self.moves = list()
        self.mymoves = list()
        
        self.level = level

    def attack1(self,other):
        self.deal_damage(other)
