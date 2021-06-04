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
from PIL import Image,ImageFont,ImageDraw
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




def owner(ctx):
    return ctx.author.id==412971313188306945

class Action(commands.Cog):
    
    def __init__(self, client):

        self.client=client

    @commands.command()
    async def hug(self, ctx, user, *, reason = None):
        r = requests.get("https://some-random-api.ml/animu/hug")
        js=r.json()
        gn=js['link']
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        embed=discord.Embed(description=f'{ctx.author.name} hugs {user}', color = random.choice(colors))
        embed.set_image(url=gn)
        if reason!=None:
            embed.description=reason
        hugtxt=['so cute...', 'sweet...', '<3']
        embed.set_footer(text=random.choice(hugtxt))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def bully(self, ctx, user = ' ', *, message = ' '):
        r = requests.get(f"https://api.waifu.pics/sfw/bully")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} bullies {user} {message}', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx, user = ' ', *, message = ' '):
        r = requests.get(f"https://api.waifu.pics/sfw/cry")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} cries {user} {message}', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, user = ' ', *, message = ' '):
        r = requests.get(f"https://api.waifu.pics/sfw/kill")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} kills {user} {message}', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)


    @commands.command()
    async def happy(self, ctx, user = ' ', *, message = ' '):
        r = requests.get(f"https://api.waifu.pics/sfw/happy")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} is happy {user} {message}', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)


    @commands.command()
    async def wink(self, ctx, user, *, message = None):
        r = requests.get(f"https://api.waifu.pics/sfw/wink")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} winks {user} {message}', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)


    @commands.command()
    async def poke(self, ctx, user = ' ', *, message = ' '):
        r = requests.get(f"https://api.waifu.pics/sfw/poke")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} pokes {user} {message}', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)





    @commands.command()
    async def cringe(self, ctx, user = ' ', *, message = ' '):
        r = requests.get(f"https://api.waifu.pics/sfw/cringe")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} cringes', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)


    @commands.command()
    async def cringe(self, ctx, user = ' ', *, message = ' '):
        r = requests.get(f"https://api.waifu.pics/sfw/cringe")
        js=r.json()
        gn=js['url']
        embed=discord.Embed(description=f'{ctx.author.name} cringes', colour=discord.Colour.red())
        embed.set_image(url=gn)
        await ctx.send(embed=embed)




#https://some-random-api.ml/animu/hug

def setup(client):
    client.add_cog(Action(client))