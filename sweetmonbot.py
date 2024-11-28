# This example requires the 'message_content' intent.
import os
import discord
from discord.ext import commands

import monsters as mon
from trainer import Trainer
import items
from battle import Battle


from dotenv import load_dotenv, dotenv_values

load_dotenv()

API_KEY = os.getenv('TOKEN')

# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)

client = commands.Bot(command_prefix="!sweet ",intents=discord.Intents.all())



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     prefix = "!sweet "
#     if message.author == client.user:
#         return

#     if message.content.startswith(prefix):
#         if message.content[len(prefix):] == "start":
#             pass
#         else:
#             print(message.content[7:])
#         await message.channel.send('OwO!')
        
        # await message.channel.send(message.content[1:])
        
# @client.event
# # async def 

@client.command(name = "sayhi")
async def hello(ctx):
    await ctx.send(f"Hello there {ctx.author.mention}")
    
@client.command(aliases=["Lol","OwO","Hi"])
async def UwU(ctx):
    await ctx.send(f"LWOLWOOWLO {ctx.author.mention}")
    


@client.command()
async def sendembed(ctx):
    embeded_msg = discord.Embed(title="Title",description="desc",color=discord.Color.green())
    embeded_msg.set_thumbnail(url=ctx.author.avatar)
    embeded_msg.add_field(name="nome",value="val",inline=False)
    embeded_msg.set_image(url=ctx.guild.icon)
    embeded_msg.set_footer(text="footertxt",icon_url=ctx.author.avatar)
    
    await ctx.send(embed=embeded_msg)

@client.command()
async def ping(ctx):
    ping_embed = discord.Embed(title ="Ping", description="OHNAWR",color=discord.Color.pink())
    ping_embed.add_field(name=f"{client.user.name}'s Latency (ms): ",value=f"{round(client.latency * 1000)} ms", inline=False)
    ping_embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
    
    await ctx.send(embed=ping_embed)

# def print_battle(player,enemy):
#     en = str(enemy).rjust(8)
    
#     print("="*20)
#     print("\n")
#     print(f"{en : >20}")
#     print("\n\n"+str(player))
#     print("\n")
#     print("="*20)

@client.command(name="select")
async def starterselect(ctx,args):
    global player
    
    player = Trainer(ctx.author.name)
    
    player.Get_Starter(args)
    
    # discord.Message()
    prefix = await client.get_prefix(ctx)

    
    # starter = discord.Embed(title="Begin your journey!",description=f"{player.active.name} has found a new home with {ctx.author.name}! You can name it with {client.get_prefix}nickname")

    await disc_print(ctx,"Begin your journey!",f"{player.active.name} has found a new home with {ctx.author.name}! You can name it with {prefix}nickname [new name]")
    
@client.command(name="nickname")
async def rename_sweetmon(ctx,*,args):
    global player
    
    player.active.nickname=args
    
    await disc_print(ctx,"Renamed!",f"Your {player.active.name} has been successfully renamed to {player.active.nickname}!")
    
    
    
    
 
@client.command(name="start")   
async def journeystart(ctx):
    # startembed = discord.Embed(title="Begin your journey!",description="Welcome to the wonderful world of Sweetmon",color=discord.Color.pink())
    # startembed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
    
    # await ctx.send(embed=startembed)
    ctx.author.add_dynamic_items()
    await disc_print(ctx,"Begin your journey!","Welcome to the wonderful world of Sweetmon")
    
    
    # await ctx.send("Welcome to the wonderful world of Sweetmon!")
    # await ctx.send("")

async def print_battle(ctx, text, battle):
    battletxt =  discord.Embed(title="Battle!",description=f"{battle.get_player1()} vs {battle.get_player2()}",color=discord.Color.pink())
    battletxt.add_field(name=f"{battle.get_player2()}\nHealth: {battle.player2.get_health()}\n\n{battle.get_player1()}\nHealth: {battle.player1.get_health()}")

    await ctx.send(embed=battletxt)

async def disc_print(ctx,title,text):
    txt = discord.Embed(title=title,description=text,color=discord.Color.pink())
    txt.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
    
    await ctx.send(embed=txt)

client.run(API_KEY)