class Battle:
    def __init__(self,player1,player2):
        """(Battle,Trainer,Trainer) -> None
        
        Initilizes a battle"""
        self.states = {"player1","player2","player1_win","player2_win"}
        self.currstate = "player1"
        
        if player1.active.speed >= player2.active.speed:
            self.player1 = player1
            self.player2 = player2
        else:
            self.player1 = player2
            self.player2 = player1
        
        self.game_over = False
        
        self.turn = 1
    
    def update(self):
        if self.all_sweetmon_fainted(self.player1):
            self.currstate = self.states[2]
            self.game_over = True
            
        if self.all_sweetmon_fainted(self.player2):
            self.currstate = self.states[3]
            self.game_over = True
            
        
    def all_sweetmon_fainted(self,player):
        for i in player.sweetmon:
            if i.health > 0:
                return False
        return True
    
    def get_player1(self):
        return str(self.player1)
    
    def get_player2(self):
        return str(self.player2)
    
    def __str__(self):
        return str(self.player2)+"\nHealth: "+self.player2.get_health()+"\n\n"+str(self.player1)+"\nHealth: "+self.player1.get_health()


from trainer import Trainer
from monsters import JollyRancher
battle = Battle(Trainer("name 1",[JollyRancher(7)]),Trainer("name 2",[JollyRancher(3)]))

print(battle)
    