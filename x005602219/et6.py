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







class Ev(commands.Cog):
    
    def __init__(self, client):

        self.client=client
    

    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name="on astrixbot.cf"))
        start=time.time()
        date_time=now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M")
        channel=self.client.get_channel(839596400149004328)
        embed=discord.Embed(title='Bot startup!', description=f'Karmatic has started at {dt_string}!', color=0xFF0000)
        embed.add_field(name='Loaded commands:', value=f'with {round(self.client.latency *1000)} ms ping!')
        await channel.send (embed=embed)
        start=time.time()
        date_time=now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M")
        print('------')
        print('Details:')
        print(f"Bot Username: {self.client.user.name}")
        print(f"BotID: {self.client.user.id}")
        print(f"Bot Ping: {round(self.client.latency *1000)} ms")
        print(f"Bot booted at {dt_string}")
        print('------')
 #       channel=self.client.get_channel(841064894282858497)







    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if not message.guild:
                channel=self.client.get_channel(840001379665969173)
                embed=discord.Embed(title='dm incoming...', description=f'"{message.content}"', colour=discord.Colour.red())
                embed.set_footer(text=f"Sent by a mortal named {message.author.name}")
                await channel.send(embed=embed)

#        await self.client.process_commands(message)




    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        print(error)
        if isinstance(error, commands.MissingPermissions):
            em=discord.Embed(title='Error!', description=f"{error}.", colour=discord.Colour.red())
#            em.add_field(name=f'Failed exception:', value=ctx)
            await ctx.send(embed=em)

        elif isinstance(error, commands.UserInputError):
            em=discord.Embed(title='Error!', description=f"{error}.", colour=discord.Colour.red())
#            em.add_field(name=f'Failed exception:', value=ctx)
            await ctx.send(embed=em)


        elif isinstance(error, commands.CommandNotFound):
            em=discord.Embed(title='Error!', description=f"{error}.", colour=discord.Colour.red())
  #          em.add_field(name=f'Failed exception:', value=ctx)
            await ctx.send(embed=em)



        elif isinstance(error, commands.BotMissingPermissions):
            em=discord.Embed(title='Error!', description=f"{error}.", colour=discord.Colour.red())
 #           em.add_field(name=f'Failed exception:', value=ctx)
            await ctx.send(embed=em)


        elif isinstance(error, commands.MissingRequiredArgument):
            em=discord.Embed(title='Error!', description=f"{error}.", colour=discord.Colour.red())
#            em.add_field(name=f'Failed exception:', value=ctx)
            await ctx.send(embed=em)


        elif isinstance(error, commands.BadArgument):
            await ctx.send("[HANDLER] Could not find that value!")


        elif isinstance(error, commands.DisabledCommand):
            em=discord.Embed(title='Error!', description=f"{error}.", colour=discord.Colour.red())
#            em.add_field(name=f'Failed exception:', value=ctx)
            await ctx.send(embed=em)


        elif isinstance(error, commands.NoPrivateMessage):
            em=discord.Embed(title='Error!', description=f"{error}.", colour=discord.Colour.red())
            em.set_footer(text='k.command (command) | for help!')
#            em.add_field(name=f'Failed exception:', value=ctx)
            await ctx.send(embed=em)


#        if isinstance(error, commands.CheckFailure):
#            await ctx.send("[HANDLER] You do not have the required role to use this command!")


def setup(client):
    client.add_cog(Ev(client))
