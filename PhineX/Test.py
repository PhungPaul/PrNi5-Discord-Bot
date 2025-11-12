import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np
import ast  # for safely parsing the list from string
import os 
from dotenv import load_dotenv

load_dotenv()

#intents settings 
intents =  discord.Intents.default()
intents.members = True
intents.message_content = True

#commands settings 
bot = commands.Bot(command_prefix="$",intents = intents)

@bot.command()
async def plot(ctx, data_str):
    try:
        # Parse the string into a Python list safely
        # Example: "[1,4,2,8]" → [1, 4, 2, 8]
        data = ast.literal_eval(data_str)

        # Ensure it's a list or tuple
        if not isinstance(data, (list, tuple)):
            await ctx.send("Please provide data in the format: `[1,2,3,...]`")
            return

        # Convert to numpy array for plotting
        data = np.array(data, dtype=float)

        # Plot
        plt.plot(data, marker='o')
        plt.title("Plot from Command")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.grid(True)

        # Save plot to file
        filename = "plot.png"
        plt.savefig(filename)
        plt.close()

        # Send file to Discord
        await ctx.send(file=discord.File(filename))

        os.remove(filename)
    except Exception as e:
        await ctx.send(f"Error parsing data: {e}\nFormat should be like: `[1,2,3,...]`")

bot.run(os.getenv('DISCORD_TOKEN'))
