import monsters as mon
import trainer
import items


def print_battle():
    en = str(enemy).rjust(8)
    
    print("="*20)
    print("\n")
    print(f"{en : >20}")
    print("\n\n"+str(player))
    print("\n")
    print("="*20)


jolly = mon.JollyRancher(5,"OwO",100,50,5)
other = mon.JollyRancher(5,name="Enemy Jolly")


##jollymon = JollyRancher(5,"OwO",100,50,5)
##othermon = Mon(5,"UwU",200,30,4)
##
player = trainer.Trainer("Samantha",[jolly])
enemy = trainer.Trainer("Computer",[other])
##
print_battle()

player.Attack1(enemy)

print_battle()
##print(enemy.sweetmon[0])
##print(player.sweetmon[0])


