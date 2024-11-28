import monsters as mon
import sweetUI as ui

class Trainer:
    def __init__(self,name,sweetmon = list(), bag = list(), has_starter=False):
        self.sweetmon = sweetmon
        self.bag = bag
        
        self.active = mon.Mon(0)
        self.activeind = 0
        self.name = name
        
        self.takenaction = False
        
        self.pc = list()
        
            

    def Get_Starter(self,num):
        starters = [mon.Croissant(5),mon.JollyRancher(5),mon.Milkshake(5)]

        self.sweetmon.clear()
        self.sweetmon.append(starters[int(num)-1])
        
        self.Switch(0,True)
        

    
    def Nickname_Sweetmon(self,sweetmon, name):
        sweetmon.nickname = name

    
    
    def Add_Sweetmon(self,sweet):
        """(Trainer,Mon) -> None
        Precondition: There must be space in party to add new sweetmon
        
        adds Sweetmon to party"""
        self.sweetmon.append(sweet)
    
    # def Action(self):
    #     if self.takenaction == True:
    #         return None
        

    def Remove_Sweetmon(self,sweetnum = -2):
        self.sweetmon.pop(sweetnum+1)

    def Attack1(self,other):
        self.active.attack1(other.active)

    def Switch(self,index,safe=False):
        self.active = self.sweetmon[index]
        self.activeind = index

    def Next(self):
        if self.activeind == 5:
            self.active = self.sweetmon[0]
            self.activeind = 0
        else:
            self.active = self.sweetmon[self.activeind+1]
            self.self.activeind = 0
    
    def get_health(self):
        return self.active.disp_health()


    def __str__(self):
        return self.name+" "+"\n\n"+str(self.activeind+1)+"/"+str(len(self.sweetmon))+" "+str(self.active)

    # def __format__(self):
    #     return "\n"+self.name+"\n\n"+str(self.activeind+1)+"/"+str(len(self.sweetmon))+" "+str(self.active)+"\n"
