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
import pickle

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
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
            except Exception as e:
                await ctx.send(f"Couldn't load cogs because:\n`{e}`", delete_after=10)
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


#self.client.unload('commands.fun')
#self.client.unload('commands.bot')
#self.client.unload('commands.mod')


    @commands.command()
    @commands.check(owner)
    async def fr(self, ctx):
        self.client.reload_extension('x005602219.b')
        self.client.reload_extension('x005602219.f')
        self.client.reload_extension('x005602219.m')
        self.client.reload_extension('x005602219.a')
        await ctx.send("Cogs reloaded.", delete_after=1)




def setup(client):
    client.add_cog(Ping(client))
