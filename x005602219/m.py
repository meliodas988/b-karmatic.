import discord
from discord.ext import commands
import asyncio






class Kick(commands.Cog):
    
    def __init__(self, client):

        self.client=client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason=reason)
    

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(ctx, member : discord.Member, *, reason = None):
        await member.ban(reason=reason)
        if reason !=None:
            print("none")
        else:
            print("reason", (reason))


    @commands.command(aliases=(['delete', 'remove', 'prune']))
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount : int = 10):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send (f"Deleted {amount} messages!")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)

    @commands.command()
    async def prefix(self, ctx, *, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = prefix

            with open('prefixes.json', 'w') as f:
                json.dump(prefixes, f, indent=4)



def setup(client):
    client.add_cog(Kick(client))