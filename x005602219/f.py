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
    async def dm(self, ctx, userid, *, dm_message):
        try:
            target = await self.client.fetch_user(userid)
            await target.send(dm_message)

            await ctx.channel.send("'" + dm_message + "' sent to: " + target.name)
        except Exception as a:
            await ctx.send(a, delete_after=5)

#            except:
#                await ctx.channel.send("Couldn't dm the given user.")
            

#        else:
#            await ctx.send("You didn't provide a user's id and/or a message.")

    @commands.command()
    async def susrate(self, ctx, *, user):
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        susnum=random.randint(1,100)
        embed=discord.Embed(title='Sus rating!', description=f'{user} is {susnum}% sus!', color = random.choice(colors))
        if susnum > 70:
            embed.set_thumbnail(url='https://i.etsystatic.com/21070033/r/il/091054/2575981808/il_570xN.2575981808_4y9n.jpg')
            embed.set_footer(text="You're very sus...")
        else:
            embed.set_thumbnail(url="https://i.redd.it/ifil63soqap51.jpg")
            embed.set_footer(text="Oh... you're not sus... damn-")
        await ctx.send(embed=embed)


    @commands.command(aliases=(['pokemongif', 'gifpoke']))
    async def pokegif(self, ctx, pokemon):
        em=discord.Embed()
        em.set_image(url=f"https://play.pokemonshowdown.com/sprites/xyani/{pokemon}.gif")
        await ctx.send(embed=em)

    @commands.command(aliases=[('chatbot', 'talk', 'bot')])
    async def cb(self, ctx, *, message):
        r = requests.get(f"https://some-random-api.ml/chatbot?message={message}&key=cOzM3rmBk3owoIWelGUvF504w")
        js=r.json()
        gn=js['response']
        await ctx.send(f"{gn}")
        

    @commands.command(aliases=(['pd', 'pokemon', 'dex']))
    async def pokedex(self, ctx, *, pokemon:str='pikachu'):
        try:
            r = requests.get(f"https://some-random-api.ml/pokedex?pokemon={pokemon}")
            a=r.json()
            aa=a['name']
            b=r.json()
            bb=b['id']
            
            ge=r.json()
            gen=ge['generation']
            embed=discord.Embed(title=f'**{aa} - #{bb}**',colour=discord.Colour.red())
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
            weight=we['weight']
            sp=r.json()
            species=sp['species'][0]
            c=r.json()
            cc=b['type'][0]
            embed.add_field(name='**Appearance:**', value=f"**Height**: {height}\n**Weight:** {weight}\n**Main Type:** {species}, {cc}", inline=False)
            desc=r.json()
            description=desc['description']
            embed.add_field(name='**Description:**', value=f"{description}", inline=False)
            im=r.json()
            img=im['sprites']['normal']
            embed.set_image(url=img)

            embed.set_thumbnail(url=ctx.author.avatar_url)
            b=r.json()
            bb=b['sprites']['animated']
            embed.set_footer(text=f"Gen {gen}. | k.pokegif {pokemon} - for {pokemon} gif!", icon_url=bb)


 #       embed.add_field(name='ID:', value=ID, inline=False)
  #      embed.add_field(name='Pokemon name:', value=aaa, inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"invalid {e}", delete_after=2)
            await asyncio.sleep(1)



    @commands.command()
    async def lyrics(self, ctx, *, search=None):
        
        if not search:
            embed = discord.Embed(title="Search a song!",)
            embed.add_field(name=f"**Example:**\n k.lyrics song name")
            await ctx.reply(embed=embed)
        
        song = search.replace(' ', '%20') 
        
        async with aiohttp.ClientSession() as lyricsSession: 
            async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: 
                if not (300 > jsondata.status >= 200):
                    await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
                else:
                    lyricsData = await jsondata.json() 
            songLyrics = lyricsData['lyrics'] 
            songArtist = lyricsData['author'] 
            songTitle = lyricsData['title']  
            
            try:
                for chunk in [songLyrics[i:i+2000] for i in range(0, len(songLyrics), 2000)]:
                    embed = discord.Embed(title=f'{songTitle}', description=chunk, color=discord.Color.blurple())
                    embed.timestamp = datetime.utcnow()
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.set_footer(text=f'by {songArtist}!')
                    await lyricsSession.close() 
                    
                    await ctx.reply(embed=embed)
                    
            except discord.HTTPException:
                embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=discord.Color.blurple())
                embed.timestamp = datetime.utcnow()
                
                await lyricsSession.close() 
                
                await ctx.reply(embed=embed)



#    @commands.command()
#    async def 



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







    @commands.command()
    async def memee(self, ctx):
        r=requests.get("https://some-random-api.ml/meme")
        me=r.json()
        meme=me['image']
        em=discord.Embed(title=f'Meme', colour=discord.Colour.red())
        em.set_image(url=meme)
        await ctx.send(embed=em)


    @commands.command(aliases=(['kitty', 'kitten', 'feline']))
    async def cat(self, ctx, type = None):
        if type == 'fact':
            r=requests.get("https://some-random-api.ml/facts/cat")
            me=r.json()
            fact=me['fact']
            em=discord.Embed(title=f'Cat fact!', description=fact, colour=discord.Colour.red())
            await ctx.send(embed=em)
        elif type=='img' or type =='image' or type == 'pic' or type=='picture':
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data=await r.json()
                    em=discord.Embed(title=f'Cat!', colour=discord.Colour.red())
                    em.set_image(url=data['file'])
                    await ctx.send(embed=em)
        elif type == None:
            r=requests.get("https://some-random-api.ml/facts/cat")
            me=r.json()
            fact=me['fact']
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data=await r.json()
                    em=discord.Embed(title=f'Cat!', description=fact, colour=discord.Colour.red())
                    em.set_image(url=data['file'])
                    await ctx.send(embed=em)
        else:
            await ctx.send("Please enter a valid usage.")



    @commands.command(aliases=(['hack']))
    async def token(self, ctx):
        r=requests.get("https://some-random-api.ml/bottoken")
        a=r.json()

        ll=a['token']
        await ctx.send("(Hacking mainframe())", delete_after=2)
        await asyncio.sleep(2)
        await ctx.send("Tracking IP", delete_after=0.4)
        await asyncio.sleep(0.4)
        await ctx.send("Tracking IP", delete_after=0.4)
        await asyncio.sleep(1)
        await ctx.send("Reading your search history", delete_after=1)
        await asyncio.sleep(1.5)
        await ctx.send("Selling your data to the government...", delete_after=2)
        await asyncio.sleep(3)
        await ctx.send("Tracking IP", delete_after=0.4)
        await asyncio.sleep(0.6)
        await ctx.send(ll)
    

    @commands.command()
    async def gayrate(self, ctx, *, user):
        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
        susnum=random.randint(1,100)
        embed=discord.Embed(title='Gay rating!', description=f'{user} is {susnum}% sus!', color = random.choice(colors))
        await ctx.send(embed=embed)

    @commands.command(aliases=[('+', 'addition')])
    async def add(self, ctx, operator):
        pass


            
        




#    @commands.command()
#    async def asl(ctx, *, anime):
#        search = AnimeSearch(anime)
#        print(search.results[0].title)




    @commands.command()
    async def ins(self, ctx):
        r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        js=r.json()
        gn=js['insult']
        await ctx.send(gn)











def setup(client):
    client.add_cog(Cfact(client))






