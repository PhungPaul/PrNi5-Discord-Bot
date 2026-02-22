import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv
import os 

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#logging 
handler = logging.FileHandler(filename='PrNi5.log', encoding='utf-8', mode='w')

#intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#command settings 
bot = commands.Bot(command_prefix='!', intents=intents)

#on_ready event response
@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")
#Hello Command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")


#Fetches Chemical data using CID
@bot.command()
async def cid(ctx, cid):
    from Utils.SearchCommand import cid_search
    await ctx.send(embed=Utils.cid_search(cid))


#Fetches Chemical Data using C_Name
@bot.command()
async def compound(ctx, *, name):
    from Utils.SearchCommand import Cname_search
    await ctx.send(embed=Cname_search(name))


#plotting chemical weight and formula 
@bot.command()
async def wplot(ctx, cid_str):
    from Utils.PlotCommand import Molecular_weight_plot

    result = Molecular_weight_plot(cid_str)
    if isinstance(result, dict):
        await ctx.send(embed=result["embed"], file=result["file"])
    else:
        await ctx.send(embed=result)



    
bot.run(token, log_handler=handler, log_level=logging.DEBUG)