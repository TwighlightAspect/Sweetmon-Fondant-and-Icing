class Trainer:
    def __init__(self,name,sweetmon = list(), bag = list()):
        self.sweetmon = sweetmon
        self.bag = bag
        self.active = self.sweetmon[0]
        self.name = name
        self.activeind = 0

    def Add_Sweetmon(self,sweet):
        if len(self.sweetmon) < 6:
            self.sweetmon.append(sweet)
        else:
            print("You have reached the max number of sweetmon")
        if len(self.sweetmon) == 1:
            self.active = self.sweetmon[0]

    def Remove_Sweetmon(self,sweetnum = -2):
        self.sweetmon.pop(sweetnum+1)

    def Attack1(self,other):
        self.active.attack1(other.active)

    def Switch(self,index):
        self.active = self.sweetmon(index)
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
