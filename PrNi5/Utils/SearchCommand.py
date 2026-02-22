import pubchempy as pcp 
import discord 

def cid_search(cid):
    try:
        cid = int(cid)

        compound = pcp.Compound.from_cid(cid)
        if compound is None:
            raise ValueError("Compound not found.")
        
        embed = discord.Embed(
            title=f"Chemical Information: CID {cid}",
            color=discord.Color.blue()
        )

        embed.add_field(name="IUPAC Name", value=compound.iupac_name or "N/A", inline=False)
        embed.add_field(name="Molecular Formula", value=compound.molecular_formula or "N/A", inline=True)
        embed.add_field(name="Molecular Weight", value=compound.molecular_weight or "N/A", inline=True)
        embed.add_field(name="SMILES", value=compound.isomeric_smiles or "N/A", inline=False)

        return embed
        
    except Exception:
        embed = discord.Embed(
            title = f"Cannot find Compound {cid}",
            color = discord.Color.red()
        )
        return embed




def Cname_search(Cname):

    try:
        compounds = pcp.get_compounds(Cname, 'name')
            
        compound = compounds[0]

        #Embed
        embed = discord.Embed(
            title=f"Chemical Information: {Cname}",
            color=discord.Color.yellow()
        )

        embed.add_field(name="IUPAC Name", value=compound.iupac_name or "N/A", inline=False)
        embed.add_field(name="Molecular Formula", value=compound.molecular_formula or "N/A", inline=True)
        embed.add_field(name="Molecular Weight", value=compound.molecular_weight or "N/A", inline=True)
        embed.add_field(name="SMILES", value=compound.isomeric_smiles or "N/A", inline=False)

        return embed
    
    except Exception:
        embed = discord.Embed(
            title = f"Cannot find Compound {Cname}",
            color = discord.Color.red()
        )
        return embed
    




