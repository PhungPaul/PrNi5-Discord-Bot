import discord
import logging 
from dotenv import load_dotenv
from discord.ext import commands
import os 

import numpy as np

#loading token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

if not token: 
    raise ValueError('Token invalid')

#logging 
handler = logging.FileHandler(filename='PhineX.log', encoding='utf-8', mode='w')

#Manual intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#commands setting
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.command()
async def roll(ctx):
    await ctx.send(np.random.randint(1,7,1))

@bot.command()
async def toss(ctx):    
    await ctx.send(np.random.choice(['Heads', 'Tails']))



bot.run(token,log_handler = handler,log_level = logging.DEBUG)