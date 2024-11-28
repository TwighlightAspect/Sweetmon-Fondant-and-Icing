import monsters as mon
from trainer import Trainer
import items
import sweetUI as ui
from battle import Battle


def get_valid_input(lst, input_str):
    while True:
        ui.typing_print(input_str)
        userinp = input().strip()
        if userinp in lst:
            return userinp
        else:
            ui.typing_print("That is an invalid input")

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
    player = Trainer(username)
    player.Get_Starter(get_valid_input(['1','2','3'],
                                       "Select a Sweetmon to be your Starter!\n\n1. Criossant\t2. Jolly Rancher\t3. Milkshake"))
    nameit = input("Nickname your "+player.sweetmon[0].name+"? y/n ").strip()
    
    if nameit == "y":
        ui.typing_print("What would you like to name it?")
        newname = input()
        player.Nickname_Sweetmon(player.sweetmon[0],newname)
        
        ui.typing_print(f"Your sweetmon is now named {newname}!")

    other = mon.JollyRancher(5,"Enemy Jolly")
    
    enemy = Trainer("Computer",[other],has_starter=True)
##
    battle = Battle(player,enemy)

    print_battle(player,enemy)

    player.Attack1(enemy)

    print_battle(player,enemy)




startjourney()


##jollymon = JollyRancher(5,"OwO",100,50,5)
##othermon = Mon(5,"UwU",200,30,4)
##


##print(enemy.sweetmon[0])
##print(player.sweetmon[0])


