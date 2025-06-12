from abc import ABC,abstractmethod

class Moves(ABC):
    def __init__(self,priority=0):
        self.prio = priority
        
    def crit(self):
        pass
    
class Attack(Moves):
    def __init__(self,power,accuracy,priority=0):
        self.power = power
        self.accuracy = accuracy
        

class Status_Moves(Moves):
    def __init__(self):
        pass