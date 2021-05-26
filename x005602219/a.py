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
    async def th(self, ctx, user : str = ' ', reason = None):
        r = requests.get("https://some-random-api.ml/animu/hug")
        js=r.json()
        gn=js['link']
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        embed=discord.Embed(title=f"{ctx.author.name} hugs {user}!", color = random.choice(colors))
        embed.set_image(url=gn)
        if reason!=None:
            embed.description=reason
        hugtxt=['so cute...', 'sweet...', '<3']
        embed.set_footer(text=random.choice(hugtxt))
        await ctx.send(embed=embed)
    



#https://some-random-api.ml/animu/hug

def setup(client):
    client.add_cog(Action(client))