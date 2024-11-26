import monsters as mon
import sweetUI as ui

class Trainer:
    def __init__(self,name,sweetmon = list(), bag = list(), has_starter=False):
        self.sweetmon = sweetmon
        self.bag = bag
        if len(self.sweetmon) >0:
            self.active = self.sweetmon[0]
            self.activeind = 0
        self.name = name
        
        
        if has_starter != True:
            self.Get_Starter()
            

    def Get_Starter(self):
        starters = [mon.Croissant(5),mon.JollyRancher(5),mon.Milkshake(5)]
        
        selection = self.get_valid_input(['1','2','3'],"Select a Sweetmon to be your Starter!\n\n1. Criossant\t2. Jolly Rancher\t3. Milkshake").strip()
        
        self.sweetmon.append(starters[int(selection)-1])
        
        nameit = input("Nickname your "+self.sweetmon[0].name+"? y/n ").strip()
        
        if nameit == "y":
            self.Nickname_Sweetmon(self.sweetmon[0])
        
        self.Switch(0,True)
    
    def Nickname_Sweetmon(self,sweetmon):
        ui.typing_print("Enter name:", end=" ")
        newname = input()
        
        sweetmon.nickname = newname
        ui.typing_print(f"your sweetmon is now named {newname}!")
    

    
    def get_valid_input(self,lst, input_str):
        while True:
            ui.typing_print(input_str)
            userinp = input()
            if userinp in lst:
                return userinp
            else:
                ui.typing_print("That is an invalid input")
    
    def Add_Sweetmon(self,sweet):
        if len(self.sweetmon) < 6:
            self.sweetmon.append(sweet)
        else:
            ui.typing_print("You have reached the max number of sweetmon")
        if len(self.sweetmon) == 1:
            self.active = self.sweetmon[0]

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


    def __str__(self):
        return "\n"+self.name+" "+str(self.active.level)+"\n\n"+str(self.active)+"\n"+str(self.activeind+1)+"/"+str(len(self.sweetmon))

    # def __format__(self):
    #     return "\n"+self.name+"\n\n"+str(self.activeind+1)+"/"+str(len(self.sweetmon))+" "+str(self.active)+"\n"
