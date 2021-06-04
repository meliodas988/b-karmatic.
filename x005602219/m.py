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




date_format = "%a, %d %b %Y %I:%M %p" 



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

    @commands.command(pass_context=True)
    async def ui(self, ctx, user: discord.Member=None):
        if not user:
            embed = discord.Embed(title="Your info.", color=0x176cd5)
            embed.add_field(name="Username", value=ctx.author.name+ "#" + ctx.message.author.discriminator + ' | ' + ctx.message.author.name, inline=True)
            embed.add_field(name="ID", value=ctx.message.author.id, inline=True)
            embed.add_field(name="Highest role", value=ctx.message.author.top_role)
            embed.add_field(name="Roles", value=len(ctx.message.author.roles))
            embed.add_field(name="Joined", value=ctx.author.joined_at.strftime(date_format))  
            embed.add_field(name="Created", value=ctx.author.created_at.strftime(date_format))
            embed.add_field(name="Bot?", value=ctx.message.author.bot)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            
        else:
            embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
            embed.add_field(name="Username", value=user.name+ "#" + ctx.message.author.discriminator + ' | ' + user.name, inline=True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Highest role", value=user.top_role)
            embed.add_field(name="Roles", value=len(user.roles))
            embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))  
            embed.add_field(name="Created", value=user.created_at.strftime(date_format))
            embed.add_field(name="Bot?", value=user.bot)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name=ctx.message.author, icon_url=user.avatar_url)
            await ctx.send(embed=embed)



    @commands.command(aliases=['make_role'])
    @commands.has_permissions(manage_roles=True)
    async def create(self, ctx, role_name, red: int = 10, green: int = 10, blue:int = 10):
        guild = ctx.guild
        await guild.create_role(name=role_name, colour=discord.Colour.from_rgb(red, green, blue))
        await ctx.send(f'Role `{role_name}` has been created')

        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, user:discord.Member, role: discord.Role):
        await user.add_roles(role)
        embed=discord.Embed(title='Role given', description=f'`{user.name}` now has `{role}`!', colour=discord.Colour.from_rgb(10, 10, 10))
        await ctx.send(embed=embed)






def setup(client):
    client.add_cog(Kick(client))