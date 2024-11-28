class Moves:
    def __init__(self,priority=0):
        self.prio = priority
    
class Attack(Moves):
    def __init__(self,power,accuracy,priority=0):
        self.power = power
        self.accuracy = accuracy
        

class Status_Moves(Moves):
    def __init__(self):
        pass