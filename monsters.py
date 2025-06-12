import random as rn
from abc import ABC,abstractmethod

class Mon(ABC):
    def __init__(self, level=0, name='placeholder', health=0, attack=0, defence=0,speed=0,exp=0):
        self.name = name
        self.nickname = name

        self.max_health = health
        self.health = health

        self.attack = attack
        self.defence = defence

        self.moves = list()
        self.mymoves = list()
        
        self.level = level
        
        self.speed = speed
        
        self.exp = exp
        self.req_exp = self.get_req_exp()
        
    def get_req_exp(self):
        return self.level ** 3
        
    def levelup(self,excess_exp):
        self.level+=1
        exp = excess_exp
        self.req_exp = self.get_req_exp()
        
    def levelstats(self):
        self.max_health += rn.randint(0,3)
        self.attack += rn.randint(0,3)
        self.defence += rn.randint(0,3)
        self.speed += rn.randint(0,3)
    
    def deal_damage(self, other):

        other.take_damage(self)
        
    def get_stats(self):
        return [self.max_health,self.attack,self.defence,self.speed,self.moves]

    def take_damage(self,other):

        self.health -= other.calculate_damage(self)

    def calculate_damage(self,other):
        return self.attack-other.defence

    def health_bar(self):
        div = self.max_health/100
        percent = int(((self.health/self.max_health)*100)/5)
        full_bar = int((self.max_health/div)/5)
        return (full_bar*"=")+"\n"+(percent*"|")+"\n"+(full_bar*"=")
    
    def disp_health(self):
        return str(self.health)+"/"+str(self.max_health)
    
    def disp_lvl(self):
        return str(self.level)
    
    @abstractmethod
    def attack1(self):
        pass

    def __str__(self):
        return self.nickname+"("+self.name+") lvl."+str(self.level)



class JollyRancher(Mon):#fire
    def __init__(self, level, name="Jolly Rancher", health=19, attack=9, defence=5,speed=13,exp=0):
        super().__init__(level,name,health,attack,defence,speed,exp)

    def attack1(self,other):
        self.deal_damage(other)

class Croissant(Mon):#grass
    def __init__(self, level, name="Criossant", health=17, attack=11, defence=3,speed=6,exp=0):
        super().__init__(level,name,health,attack,defence,speed,exp)

    def attack1(self,other):
        self.deal_damage(other)
        
class Milkshake(Mon):#water
    def __init__(self, level, name="Milk Shake", health=18, attack=10, defence=4,speed=20,exp=0):
        super().__init__(level,name,health,attack,defence,speed,exp)

    def attack1(self,other):
        self.deal_damage(other)