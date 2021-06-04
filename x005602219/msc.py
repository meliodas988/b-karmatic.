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


class Msc(commands.Cog):
    
    def __init__(self, client):

        self.client=client

    @commands.command()
    async def tts(self, ctx, *, message):
        channel = self.client.get_channel(845427696472555532)
        embed=discord.Embed(title=f'Message from {ctx.author.name}', description=message, colour=discord.Colour.from_rgb(10, 11, 10))

        img=Image.open("images/whitee.png")
        draw=ImageDraw.Draw(img)
        font=ImageFont.truetype("fonts/font.otf", 30)
        draw.text((313,260), message, (10,10,10), font=font)
        img.save("images/AAA.PNG")
#        await ctx.reply(file = discord.File("images/AAA.PNG"))
        em=discord.Embed(title=f'Message from {ctx.author.name}', description=message, colour=discord.Colour.from_rgb(10, 11, 10))
#        em.set_image(url='https://replit.com/@zorozoro1/b-karmatic#images/AAA.PNG')
        await channel.send(embed=embed)
        await ctx.reply(embed=em)



    @commands.command()
    async def ttw(self, ctx, *, message):
        channel = self.client.get_channel(845427554852405309)
        embed=discord.Embed(title=f'Message from {ctx.author.name}', description=message, colour=discord.Colour.from_rgb(10, 11, 10))

        img=Image.open("images/whitee.png")
        draw=ImageDraw.Draw(img)
        font=ImageFont.truetype("fonts/font.otf", 30)
        draw.text((313,260), message, (10,10,10), font=font)
        img.save("images/AAA.PNG")
        await ctx.reply(file = discord.File("images/AAA.PNG"))
#        em=discord.Embed(title=f'Message from {ctx.author.name}', description=message, colour=discord.Colour.from_rgb(10, 11, 10))
        await channel.send(embed=embed)
#        await ctx.reply(embed=em)







def setup(client):
   client.add_cog(Msc(client))