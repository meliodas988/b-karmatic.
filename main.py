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






messages = joined = 0


#https://discord.com/api/oauth2/authorize?client_id=821393463484481536&permissions=0&scope=bot
#823680910573961218

ecolors=["red", "pink", "yellow"]

os.system("clear")
 

status_num=random.randint(1,1000)



client = commands.Bot(command_prefix = 'k.', ownerid='412971313188306945', description='Yes', help_command=None)


#pickle start

dataFilename='data.pickle'

class Data():
    def __init__(self, wallet, bank):
        self.wallet=wallet
        self.bank = bank




#pickle end


#/////////////////////////cogs///////////////////////////////
cogs=['commands.vc', 'commands.fun.message', 'commands.bot.ping', 'commands.fun.president', 'commands.fun.num-fun', 'commands.music', 'commands.mod.purge', 'commands.mod.util', 'commands.fun.facts']


#for cog in cogs:
#    try:
#        client.load_extension(cog)
#    except Exception as e:
#        print(f"Can't load cog {cog}: {str(e)}")

client.load_extension('x005602219.f')
client.load_extension('x005602219.b')
client.load_extension('x005602219.m')
client.load_extension('x005602219.a')







@client.event
async def on_member_join():
    global join
    join += 1



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="On console messing with bat files- hehe~ "))
    start=time.time()
    date_time=now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    channel=client.get_channel(839596400149004328)
    embed=discord.Embed(title='Bot startup!', description=f'Karmatic has started at {dt_string}!', color=0xFF0000)
    embed.add_field(name='Loaded commands:', value=f'with {round(client.latency *1000)} ms ping!')
    await channel.send (embed=embed)
    start=time.time()
    date_time=now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    print('------')
    print('Details:')
    print(f"Bot Username: {client.user.name}")
    print(f"BotID: {client.user.id}")
    print(f"Bot Ping: {round(client.latency *1000)} ms")
    print(f"Bot booted at {dt_string}")
    print('------')
    channel=client.get_channel(841064894282858497)
    await channel.send (f"```New Bootup at {dt_string}```")






@client.event
async def on_message(message):
    global messages
    messages += 1
    if not message.author.bot:
        if not message.guild:
            channel=client.get_channel(840001379665969173)
            embed=discord.Embed(title='Karmatic dm incoming...', description=f'"{message.content}"', colour=discord.Colour.red())
            embed.set_footer(text=f"Sent by a mortal named {message.author.name}")
            await channel.send(embed=embed)

    await client.process_commands(message)








#@client.event
#async def update_stats():
#    await client.wait_until_ready()
#    global messages, joined#
#
#    while not client.is_closed():
#        try:
#            with open("stats.txt", 'a') as f:
#                date_time=now = datetime.now()
#                dt_string = now.strftime("%d/%m/%Y %H:%M")
#                f.write(f"""\n
#    At: {dt_string}\n
#    Messages sent: {messages}\n 
#    Members joined: {joined}\n________________________""")
#            messages = 0
#            joined = 0
            
##            await asyncio.sleep(300)
#        except Exception as e:
#            print(e)

def aaaaa():
    @client.command()
#    @commands.is_owner()
    async def guilds(ctx):
        for guilds in client.guilds():
            print(guilds)

############################################

@client.command(alieses=["framed"])
async def frame(ctx, user: discord.Member = None):
  if user == None:
    user=ctx.author
    
  trump=Image.open("images/no one.png")
  
  asset=user.avatar_url_as(size=128)
    
  data=BytesIO(await asset.read())
  
  pfp=Image.open(data)
  
  pfp=pfp.resize((600, 600))  #289 173#

  trump.paste( pfp, (0, 0))
  trump.save("images/no one save.png")

  await ctx.send(file=discord.File("images/no one save.png"))
  channel=client.get_channel(839596400149004328)

  date_time=now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  embed=discord.Embed(title= f"{ctx.author} has used the no one meme command at {dt_string}!",colour=discord.Colour.red())
  
  embed.add_field(name="message sent:", value =f"k.president! {user}", inline=True)
  await channel.send(embed=embed)

@client.command()
async def dog(ctx):
    rdog=random.randint(1,1000)
    embed=discord.Embed(title='Dog!')
    embed.set_image(url=f'https://placedog.net/{rdog}')
    await ctx.send(embed=embed)


@client.command()
async def text(ctx, *, text = 'HMMM... SUS-'):
  img=Image.open("images/aa.PNG")
  draw=ImageDraw.Draw(img)
  font=ImageFont.truetype("fonts/font.otf", 24)
  draw.text((100,45), text, (248,248,255), font=font)
  img.save("images/AAA.PNG")
  await ctx.send(file = discord.File("images/AAA.PNG"))
  channel=client.get_channel(839596400149004328)
  date_time=now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  embed=discord.Embed(title= f"{ctx.author} has used the text command at {dt_string}!",colour=discord.Colour.red())
  
  embed.add_field(name="message sent:", value = f"k.text {text}", inline=True)
  await channel.send(embed=embed)
  
#  await channel.send(f"{ctx.author} has used the text command!")








#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.discord.ActivityType.name="to wolfies moans "))



#	await client.change_presence(status=discord.Status.dnd, activity=activity)
#@client.event
#async def smsg(cxt):
  




@client.command()
async def aal(ctx):
  numer=random.randint(1,100)
  embed=discord.Embed(title= f"Your number is {numer}!",colour=discord.Colour.red())
  await ctx.send(embed=embed)
  channel=client.get_channel(839596400149004328)
  embed=discord.Embed(title=(f"{ctx.author}  has just used the command:"), description=f'{ctx}')
  await channel.send(embed=embed)












@client.command()
async def pichupic(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://pokeapi.co/api/v2/pokemon/pichu") as r:
            data=await r.json()

            embed=discord.Embed(title='pichu picture!', colour=discord.Colour.red())
            embed.set_image(url=data['abilities'])
            await ctx.send (embed=embed)



  
@client.command()
async def lyrics(ctx, *, search=None):
    """A command to find lyrics easily!"""
    
    if not search: # if user hasnt typed anything, throw a error
        embed = discord.Embed(title="No search argument!", description="You havent entered anything, so i couldnt find lyrics!")
        await ctx.reply(embed=embed)
        
        # ctx.reply is available only on discord.py 1.6.0!
        
    song = search.replace(' ', '%20') # replace spaces with "%20"
    
    async with aiohttp.ClientSession() as lyricsSession: # define session
        async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: # define json data
            if not (300 > jsondata.status >= 200):
                await ctx.send(f'Recieved Poor Status code of {jsondata.status}.')
            else:
                lyricsData = await jsondata.json() # load json data
        songLyrics = lyricsData['lyrics'] # the lyrics
        songArtist = lyricsData['author'] # the authors name
        songTitle = lyricsData['title'] # the songs title
        
        try:
            for chunk in [songLyrics[i:i+2000] for i in range(0, len(songLyrics), 2000)]: # if the lyrics extend the discord character limit (2000): split the embed
                embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=discord.Color.blurple())
                embed.timestamp = datetime.utcnow()
                
                await lyricsSession.close() # closing the session
                
                await ctx.reply(embed=embed)
                
        except discord.HTTPException:
            embed = discord.Embed(title=f'{songTitle} by {songArtist}', description=chunk, color=discord.Color.blurple())
            embed.timestamp = datetime.utcnow()
            
            await lyricsSession.close() # closing the session
            
            await ctx.reply(embed=embed)










@client.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("http://aws.random.cat/meow") as r:
            data=await r.json()

            embed=discord.Embed(title='Cat picture! :cat:', colour=discord.Colour.red())
            embed.set_image(url=data['file'])
            await ctx.send (embed=embed)









@client.command(aliases=["commands", "command"])
async def helpr(ctx):
  embed=discord.Embed(title="Help commands:", color= discord.Color.red())
  embed.add_field(name="Moderation", value = 'Kick, Ban', inline=True)
  embed.add_field(name="fun", value = 'Gayrate, President, pain, susrate', inline=True)
  embed.add_field(name="Moderation", value = 'Kick, Ban', inline=True)


  embed.set_footer(text='Say "k.<command>"!')
  await ctx.send(embed=embed)




##################################

@client.command(aliases=["rategay", "gayrate"])
async def howgay(ctx):
  gayperc=random.randint(1,100)
  embed=discord.Embed(title="gay rate", color= discord.Color.red())
  embed.add_field(name="Your gay rating is:", value = f"You are {gayperc}% gay.", inline=True)
#  await ctx.send(embed=embed)
 # embed.add_field(name="yes", value="value")

  await ctx.send(embed=embed)


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def ttt(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":one:", ":two:", ":three:",
                 ":four:", ":five:", ":six:",
                 ":seven:", ":eight:", ":nine:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":one:" or 0 < pos < 10 and board[pos - 1] == ":two:" or 0 < pos < 10 and board[pos - 1] == ":three:" or 0 < pos < 10 and board[pos - 1] == ":four:" or 0 < pos < 10 and board[pos - 1] == ":five:" or 0 < pos < 10 and board[pos - 1] == ":six:" or 0 < pos < 10 and board[pos - 1] == ":seven:" or 0 < pos < 10 and board[pos - 1] == ":eight:" or 0 < pos < 10 and board[pos - 1] == ":nine:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ttt.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


























#economy
@client.command()
async def gimmemoney(message):
    memberData=loadMemberData(message.author.id)

    memberData.wallet+=1
    await message.channel.send("You have gained 1 coin")
    savememberdata(message.author.id, memberData)

@client.command()
async def bal(message):
    memberData=loadMemberData(message.author.id)
    embed=discord.Embed(title="{member}'s Balance:".format(member=message.author.display_name, colour=discord.Colour.from_rgb(0, 255, 0)))
    embed.add_field(name='wallet :dollar:', value=str(memberData.wallet))
    embed.add_field(name='bank :moneybag:', value=str(memberData.bank))
    await message.channel.send(embed=embed)


@client.command()
async def wallet(message):
    memberData=loadMemberData(message.author.id)
    embed=discord.Embed(title="{member}'s Wallet Balance:".format(member=message.author.display_name, colour=discord.Colour.from_rgb(0, 255, 0)))
    embed.add_field(name='wallet :dollar:', value=str(memberData.wallet))
    await message.channel.send(embed=embed)

@client.command()
async def bank(message):
    memberData=loadMemberData(message.author.id)
    embed=discord.Embed(title="{member}'s Bank Balance:".format(member=message.author.display_name, colour=discord.Colour.from_rgb(0, 255, 0)))
    embed.add_field(name='bank :moneybag:', value=str(memberData.bank))
    await message.channel.send(embed=embed)


def loadData():
    if os.path.isfile(dataFilename):
        with open (dataFilename, 'rb') as file:
            return pickle.load(file)
    else:
        return dict()
def loadMemberData(memberID):
    data = loadData()
    if memberID not in data:
        return Data(0, 0)
    return data[memberID]

def savememberdata(memberID, memberData):
    data=loadData()

    data[memberID] = memberData
    with open(dataFilename, 'wb') as file:
        pickle.dump(data, file)












keep_alive()

#client.loop.create_task(update_stats())
client.run(os.getenv('token'))

