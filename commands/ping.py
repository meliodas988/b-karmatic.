import discord
from discord.ext import commands

class Ping(commands.Cog):
    
    def __init__(self, client):

        self.client=client

    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed(title='Ping!', description=f"{round(self.client.latency *1000)}ms latency!",color= discord.Color.red())
        await ctx.send(embed=embed)





#@client.command(aliases=["pong"])
#async def ping(ctx):
#  await ctx.send (f"{round(client.latency *1000)}ms")
#  embed=discord.Embed(title='Ping!', description='Pong! The bots latency is:',color= discord.Color.red())
#  embed.add_field(name=f"{round(client.latency *1000)}ms", value=f"peachi > apple", inline=True)
#  await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Ping(client))