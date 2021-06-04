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
from discord import Member, utils
from replit import db





os.system("clear")



intents = discord.Intents(messages=True, guilds=True,members=True)
client = commands.Bot('k.', owner_id='412971313188306945', description='Yes',help_command=None, intents=intents)


#/////////////////////////cogs///////////////////////////////

client.load_extension('x005602219.f')
client.load_extension('x005602219.b')
client.load_extension('x005602219.m')
client.load_extension('x005602219.a')
#client.load_extension('x005602219.et6')
client.load_extension('x005602219.text')
client.load_extension('x005602219.lc')
client.load_extension('x005602219.vc')
#client.load_extension("x005602219.msc")

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


  
#  await channel.send(f"{ctx.author} has used the text command!"



@client.command()
async def onlinem(ctx):
    await ctx.send(len([member for member in ctx.guild.members if not member.bot and discord.Status.offline]))


##################################



@client.command()
async def an(ctx, num: int):
    db["money"] += num
    await ctx.send(f"{num} is done!")

@client.command()
async def bal(ctx):
    val=db['money']
    await ctx.send(val)

@client.command()
async def kli(ctx):
    ll=db.keys()
    await ctx.send(ll)

@client.command()
async def delkey(ctx, key):
    del db[key]




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












keep_alive()
client.run(os.getenv('token'))