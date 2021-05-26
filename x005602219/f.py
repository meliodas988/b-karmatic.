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
import io






class Cfact(commands.Cog):
    
    def __init__(self, client):

        self.client=client
    
    @commands.command()
    async def fact(self, ctx, type: str = 'a'):
        type.lower()

        if type=='panda':
            r = requests.get("https://some-random-api.ml/facts/panda")
            js=r.json()
            gn=js['fact']
            await ctx.send(gn)
        



    @commands.command(aliases=['mimic', 'repeat', 'copy'])
    async def say(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        await ctx.send(message)

    
    @commands.command(aliases=["quote", 'array', 'list'])
    async def script(self, ctx, *args):
        await ctx.channel.purge(limit=1)
        await ctx.send(args)


    @commands.command(aliases=(['rn', 'randnum', 'randomnumber']))
    async def randomnum(self, ctx, num = 10):
        rrnum=random.randint(1, (num))
        embed=discord.Embed(title='Random number!', description=f'Your number is: {rrnum}!', colour=discord.Colour.red())
        await ctx.send(embed=embed)

    @commands.command()
    async def hi(ctx):
        await ctx.send("Hi")


    @commands.command()
    async def dm(self, ctx, user_id=None, *, args=None):
        if user_id != None and args != None:
            try:
                target = await self.client.fetch_user(user_id)
                await target.send(args)

                await ctx.channel.send("'" + args + "' sent to: " + target.name)

            except:
                await ctx.channel.send("Couldn't dm the given user.")
            

        else:
            await ctx.send("You didn't provide a user's id and/or a message.")

    @commands.command()
    async def susrate(self, ctx, user : discord.Member = None):
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        susnum=random.randint(1,100)
        embed=discord.Embed(title='Sus rating!', description=f'<@{user.id}> is {susnum}% sus!', color = random.choice(colors))
        if susnum > 70:
            embed.set_thumbnail(url='https://i.etsystatic.com/21070033/r/il/091054/2575981808/il_570xN.2575981808_4y9n.jpg')
            embed.set_footer(text="You're very sus...")
        else:
            embed.set_thumbnail(url="https://i.redd.it/ifil63soqap51.jpg")
            embed.set_footer(text="Oh... you're not sus... damn-")
        await ctx.send(embed=embed)


    @commands.command()
    async def aun(self, ctx):
        await ctx.send(ctx.author.name)

    @commands.command(aliases=(['pokemongif', 'gifpoke']))
    async def pokegif(self, ctx, pokemon:str=None):
        if pokemon==None:
            embed=discord.Embed(title="Invalid usage.", description='Please enter a pokemons name.')
            embed.add_field(name='usage Example:', value='k.pokegif pikachu')
        else:
            await ctx.send(f"https://play.pokemonshowdown.com/sprites/xyani/{pokemon}.gif")

    @commands.command()
    async def cb(self, ctx, message):
        r = requests.get(f"https://some-random-api.ml/chatbot?message={message}&key=cOzM3rmBk3owoIWelGUvF504w")
        js=r.json()
        gn=js['response']
        await ctx.send(gn)
        

    @commands.command()
    async def pkd(self, ctx, pokemon:str='pikachu'):
        r = requests.get(f"https://some-random-api.ml/pokedex?pokemon={pokemon}")
        a=r.json()
        aa=a['name']
        b=r.json()
        bb=b['id']
        c=r.json()
        cc=b['type'][0]
        ge=r.json()
        gen=ge['generation']
        embed=discord.Embed(title=f'{aa} - #{bb}', description=f'**Main Type:** {cc}\n**generation:** {gen}',colour=discord.Colour.red())
        c=r.json()
        hp=c['stats']['hp']
        d=r.json()
        attack=d['stats']['attack']
        e=r.json()
        def_=e['stats']['defense']
        f=r.json()
        spatk=f['stats']['sp_atk']
        h=r.json()
        spdef=h['stats']['sp_def']
        i=r.json()
        spd=i['stats']['speed']
        j=r.json()
        ttl=j['stats']['total']
        embed.add_field(name='**Base stats:**', value=f"**Hp:** {hp} \n**Attack:** {attack}\n**Defense:** {def_} \n**Sp. Atk:** {spatk}\n**Sp. Def:** {spdef} \n**Speed** {spd}\n**Total:** {ttl} ", inline=False)
        he=r.json()
        height=he['height']
        we=r.json()
        weight=we['height']
        sp=r.json()
        species=sp['species'][0]
        embed.add_field(name='**Appearance:**', value=f"{height}**\n****Weight:** {weight}\n**Main Species:**{species}", inline=False)
        desc=r.json()
        description=desc['description']
        embed.add_field(name='**Description:**', value=f"{description}", inline=False)
        im=r.json()
        img=im['sprites']['normal']
        embed.set_image(url=img)

        embed.set_thumbnail(url=ctx.author.avatar_url)
        b=r.json()
        bb=b['sprites']['animated']
        embed.set_footer(text=f"k.pokegif - for full pokemon gif!", icon_url=bb)

 #       embed.add_field(name='ID:', value=ID, inline=False)
  #      embed.add_field(name='Pokemon name:', value=aaa, inline=False)
        await ctx.send(embed=embed)





    @commands.command()
    async def triggered(self, ctx, member:
        discord.Member=None):
            if not member: # if no member is mentioned
                member = ctx.author # the user who ran the command will be the member
                
            async with aiohttp.ClientSession() as wastedSession:
                async with wastedSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
                    imageData = io.BytesIO(await wastedImage.read())
                    
                    await wastedSession.close()
                    
                    await ctx.reply(file=discord.File(imageData, 'triggered.gif'))
























def setup(client):
    client.add_cog(Cfact(client))






