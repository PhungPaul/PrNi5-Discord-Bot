import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pubchempy as pcp
import ast
import discord

def Molecular_weight_plot(cid_str):

    try:
        cid_list = ast.literal_eval(cid_str)

        df = pd.DataFrame([
            {
                "Molecular Formula": compound.molecular_formula,
                "Molecular Weight": float(compound.molecular_weight)
            }
            for compound in (pcp.Compound.from_cid(cid) for cid in cid_list)
        ])

        sns.scatterplot(data=df, x = 'Molecular Weight', y = 'Molecular Formula')

        plt.tight_layout()
        plt.savefig("plot.png")
        plt.close()

        file = discord.File('plot.png', filename = 'plot.png')
        embed =  discord.Embed(title = "Molecular Weight plot", color=discord.Color.blue())
        embed.set_image(url="attachment://plot.png")

        return {"embed": embed, "file": file}

    except Exception as e:
        return discord.Embed(
            title = f"Error: {e}",
            color = discord.Color.red()
        )