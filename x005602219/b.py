#///////imports\\\\\\\\#
import discord
import random
import json
from discord.ext import commands
import asyncio
import time
import requests
import os
from os import sys
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from datetime import datetime
from itertools import cycle
import aiohttp
from aiohttp import request
import math
import traceback
import praw
from webserver import keep_alive


cogs = ['b', 'f', 'm', 'a']


def owner(ctx):
    return ctx.author.id == 412971313188306945


class Ping(commands.Cog):
    def __init__(self, client):

        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title='Ping!',
            description=f"{round(self.client.latency *1000)}ms latency!",
            color=discord.Color.red())
        await ctx.send(embed=embed)

    @commands.command()
    async def cmds(self, ctx):
        await ctx.send(self.get_commands())


    @commands.command()
    @commands.check(owner)
    async def reload(self, ctx, cog: str = 'all'):
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)
        if cog == 'all':
            try:
                await asyncio.sleep(2)
                await ctx.send(f"Reloading all cogs.", delete_after=0.5)
                await asyncio.sleep(0.5)
                await ctx.send(f"Reloading all cogs..", delete_after=0.5)
                await asyncio.sleep(1)
                await ctx.send(f"Reloading all cogs...", delete_after=0.5)
                await asyncio.sleep(4)
                await ctx.send("cogs reloaded succesfully.", delete_after=3)
                self.client.reload_extension('x005602219.b')
                self.client.reload_extension('x005602219.f')
                self.client.reload_extension('x005602219.m')
                self.client.reload_extension('x005602219.a')
                self.client.reload_extension('x005602219.text')
                self.client.reload_extension('x005602219.et6')
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
            except Exception as e:
                await ctx.send(f"Couldn't load cogs because:\n{e}", delete_after=10)
        else:
            try:
                await asyncio.sleep(1)
                await ctx.send(f"Reloading {cog}...", delete_after=1)
                self.client.reload_extension(f'x005602219.{cog}')
                await asyncio.sleep(2)
                await ctx.send(f"{cog} has been loaded.", delete_after=3)
            except Exception as e:
                await ctx.send(f"Extension {cog} has not been reloaded because:\n{e}", delete_after=4)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)

    @commands.command()
    @commands.check(owner)
    async def load(self, ctx, cog: str = 'all'):
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)
        try:
            await asyncio.sleep(1)
            await ctx.send(f"loading {cog}...", delete_after=1)
            self.client.load_extension(f'x005602219.{cog}')
            await asyncio.sleep(2)
            await ctx.send(f"loading {cog}...", delete_after=3)
            await ctx.send(f"loaded {cog}", delete_after=3)            
        except Exception as e:
            await ctx.send(f"Extension {cog} has not been loaded because:\n{e}.", delete_after=8)
            print(e)
            await asyncio.sleep(2)

    @commands.command()
    @commands.check(owner)
    async def unload(self, ctx, cog: str = 'all'):
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)
        try:
            await asyncio.sleep(1)
            await ctx.send(f"unloading {cog}...", delete_after=1)
            self.client.unload_extension(f'x005602219.{cog}')
            await asyncio.sleep(2)
        except Exception as e:
            await ctx.send(f"Extension {cog} has not been unloaded.",
                           delete_after=4)
            print(e)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)

    @commands.command()
    async def invite(self, ctx):
        await ctx.send(
            "https://discord.com/api/oauth2/authorize?client_id=821393463484481536&permissions=0&scope=bot"
        )


    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 412971313188306945: 
            print("shutdown")
            try:
                await self.client.close()
            except:
                print("EnvironmentError")
                self.client.clear()
        else:
            await ctx.send("You do not own this bot!")

#self.client.unload('commands.fun')
#self.client.unload('commands.bot')
#self.client.unload('commands.mod')


    @commands.command()
    @commands.check(owner)
    async def fr(self, ctx):
        try:
            await ctx.channel.purge(limit=1)
            self.client.reload_extension('x005602219.b')
            self.client.reload_extension('x005602219.f')
            self.client.reload_extension('x005602219.m')
            self.client.reload_extension('x005602219.a')
            self.client.reload_extension('x005602219.et6')
            self.client.reload_extension('x005602219.text')
            self.client.reload_extension('x005602219.lc')
            self.client.reload_extension('x005602219.vc')
            self.client.reload_extension('x005602219.msc')
        except Exception as l:
            await ctx.send(l)
#            raise Exception
#            await ctx.send(Exception)
#        except Exception as e:
#            
#            await ctx.send(e, delete_after=5)
#            if e == None:
#                await ctx.send("Cogs reloaded.", delete_after=2)
        




def setup(client):
    client.add_cog(Ping(client))
