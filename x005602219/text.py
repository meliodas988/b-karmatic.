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






class Txt(commands.Cog):
    
    def __init__(self, client):

        self.client=client


    @commands.command()
    async def text(self, ctx, *, text = 'HMMM... SUS-'):
        img=Image.open("images/white.jpg")
        draw=ImageDraw.Draw(img)
        font=ImageFont.truetype("fonts/font.otf", 24)
        draw.text((100,45), text, (248,248,255), font=font)
        img.save("images/AAA.PNG")
        await ctx.send(file = discord.File("images/AAA.PNG"))


def setup(client):
    client.add_cog(Txt(client))