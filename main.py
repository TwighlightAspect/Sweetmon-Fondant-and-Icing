import monsters as mon
import trainer
import items
import sweetUI as ui


def print_battle(player,enemy):
    en = str(enemy).rjust(8)
    
    print("="*20)
    print("\n")
    print(f"{en : >20}")
    print("\n\n"+str(player))
    print("\n")
    print("="*20)

def startjourney():
    ui.typing_print("Welcome to the wonderful world of sweetmon! What did you say your name was? ",end="")
    username =input()
    ui.typing_print(f"Ahh {username}, such a beautiful name!")
    ui.typing_print("Before you go, this world is too dangerous to travel alone. Luckily for you I have a few sweetmon you can select from to accompany you on your journey!\n")
    player = trainer.Trainer(username)
    
    other = mon.JollyRancher(5,"Enemy Jolly")
    
    enemy = trainer.Trainer("Computer",[other],has_starter=True)
##
    print_battle(player,enemy)

    player.Attack1(enemy)

    print_battle(player,enemy)




startjourney()


##jollymon = JollyRancher(5,"OwO",100,50,5)
##othermon = Mon(5,"UwU",200,30,4)
##


##print(enemy.sweetmon[0])
##print(player.sweetmon[0])


