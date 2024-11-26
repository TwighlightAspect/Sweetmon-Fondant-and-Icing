# This example requires the 'message_content' intent.
import os
import discord

import monsters as mon
import trainer
import items


from dotenv import load_dotenv, dotenv_values

load_dotenv()

API_KEY = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!sweet'):
        if message.content[7:] == "start":
            await message.channel.send("Welcome to the wonderful world of sweetmon! What did you say your name was? ")
            playername =await client.wait_for("message", timeout = 30)
            await message.channel.send("Ahh "+str(playername.content)+", such a beautiful name!")
            await message.channel.send("Before you go, this world is too dangerous to travel alone. Luckily for you I have a few sweetmon you can select from to accompany you on your journey!\n")
            player = trainer.Trainer(playername.content)
            
            other = mon.JollyRancher(5,"Enemy Jolly")
            
            enemy = trainer.Trainer("Computer",[other],has_starter=True)
        ##
            print_battle(player,enemy)

            player.Attack1(enemy)

            print_battle(player,enemy)
        else:
            print(message.content[7:])
        await message.channel.send('OwO!')
        
        # await message.channel.send(message.content[1:])

def print_battle(player,enemy):
    en = str(enemy).rjust(8)
    
    print("="*20)
    print("\n")
    print(f"{en : >20}")
    print("\n\n"+str(player))
    print("\n")
    print("="*20)
    
async def journeystart():
    pass

client.run(API_KEY)