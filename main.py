

#///////imports\\\\\\\\#
import discord
import random
import tkinter as tk
import json
from discord.ext import commands, tasks
import asyncio
import time
import requests
import os
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO
from datetime import datetime
from itertools import cycle
import aiohttp
from aiohttp import request





ecolors=["red", "pink", "yellow"]

os.system("clear")
 

 
client = commands.Bot(command_prefix = 'k.', help_command=None)
status = cycle(["without a dad", "under my bed", "with senpai sentinel X", "with sentinel x action figures!", "alone..."])


#client.load_extension("commands.ping")


cogs=['commands.ping']



for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f"Can't load cog {cog}: {str(e)}")


@client.command()
async def mcol(ctx):
    embed=discord.Embed(title='Hey', colour=discord.Colour.random.choice[("red","yellow")]())
    await ctx.send (embed=embed)
    

def loadcmds():
    for command in client.commands:
        print(f"Loaded: {command}")




#     start = time.time()
#     print("hello")
#     end = time.time()
#     print(end - start)

@client.event
async def on_ready():
    start=time.time()
    changest.start()
    activity=discord.Game(name="on wolfie", type=3)
#  await client.change_presence(status=discord.Status.dnd,)
    date_time=now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    channel=client.get_channel(839596400149004328)
    embed=discord.Embed(title='Bot startup!', description=f'Karmatic has started at {dt_string}!', color=0xFF0000)
    embed.add_field(name='Loaded commands:', value=f'with {round(client.latency *1000)} ms ping!')
    await channel.send (embed=embed)
    print('------')
    print('Details:')
    print(f"Bot Username: {client.user.name}")
    print(f"BotID: {client.user.id}")
    print(f"Bot Ping: {round(client.latency *1000)} ms")
    print('------')
    channel=client.get_channel(841064894282858497)
    await channel.send (((f"""```
        New Bootup at {dt_string}
        ```""")))
    for command in client.commands:
        channel=client.get_channel(841064894282858497)
        await channel.send(f"`Loaded: {command}`")
    end=time.time()
    await channel.send(f"""```
    Commands loaded in {round(end-start)} seconds!
   ``` """)


#        configactivity = config['bot_activity']





#  await channel.send(f"Karmatic.py has succesfully started up! at {dt_string}")


@tasks.loop(seconds=1)
async def changest():
  await client.change_presence(activity=discord.Game(next(status)))
#  channel=client.get_channel(839659864426020875)
#  await channel.send(f"Karmatic's new status is {status}")

#########################################################



#@client.event
#async def on_member_join(member):
#  channel=client.get_channel(839659864426020875)
#  embed=discord.Embed(title='new member', description=f'the member {member} just joined!')
#  await channel.send(embed=embed)
 # with open('ulvl.json', 'r') as f:
  #  users=json.load(f)

  #await update_data(users, member)

#  with open("users.json", "w") as f:
 #   json.dump(users, f)


#@client.event
#async def on_message(message):
 # with open('users.json', 'r') as f:
  #  users=json.load(f)
  #await update_data(users, message.author)
#  await add_experience(users, message.author, 5)
 # await level_up(users, message.author, message.channel)
  #with open("users.json", "w") as f:
 #   json.dump(users, f)
#async def update_data(users, user):
 # if not user.id in users:
  #  users[user.id] = {}
   # users[user.id]['experience'] = 0
    #users[user.id]['level'] = 1
#    users[user.id]['name'] = username

#async def add_experience(users, user, experience):
 # users[user.id]['experience'] += experience

#async def level_up(users, user, channel):
 # experience=users[user.id]['experience']
  #lvl_start=users[user.id]['level']
  #lvl_end=int(experience ** (1/4))

  #if lvl_start < lvl_end:
   #await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
  # users[user.id]['level'] = lvl_end



##########################################################















@client.command()
async def bal(ctx):
  await open_acc(ctx.author)


@client.event
async def on_member_join(member: discord.Member = None):
    channel=client.get_channel(840001451400233000)
    await channel.send("Member joined")
    print("member {member} joined!")


async def open_acc(user):
  with open("bal.json", 'r') as f:
    users=json.load(f)
  

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)]['bal'] = 0
    users[str(user.id)]['bank'] = 0











#date_time=now = datetime.now()
#  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
 # embed=discord.Embed(title= f"{ctx.author} has used the text command at {dt_string}!",colour=discord.Colour.red())
  
#  embed.add_field(name="message sent:", value = f"k.text {text}", inline=True)
 # await channel.send(embed=embed)




@client.command()
async def raltsstats(ctx):
    embed=discord.Embed(Title='Level 13 Ralts')
    embed.add_field(name='**Level 16 Ralts**',value='**Details**', inline=True)
    embed.add_field(name='XP:', value='0/575', inline=False)
    embed.set_image(url='https://poketwo.s3.object1.us-east-1.tswcloud.com/data/images/280.png?v=26')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/412971313188306945/9ed4de33ce4408d88fe3f558388be207.png?size=1024')
    await ctx.send (embed=embed)






@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)

@clear.error
async def clrerror(ctx, error):
  await ctx.send("no")



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, amount : int):
  await ctx.channel.purge(limit=amount)

@purge.error
async def purgerror(ctx, error):
  await ctx.send("no")



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def delete(ctx, amount : int):
  await ctx.channel.purge(limit=amount)

@delete.error
async def deleterror(ctx, error):
  await ctx.send("no")









@client.command(alieses=["pres", "trumpify"])
async def president(ctx, user: discord.Member = None):
  if user == None:
    user=ctx.author
    
  trump=Image.open("images/donald.jpg")
  
  asset=user.avatar_url_as(size=128)
    
  data=BytesIO(await asset.read())
  
  pfp=Image.open(data)
  
  pfp=pfp.resize((561, 765))  #289 173#

  trump.paste( pfp, (289, 173))
  trump.save("images/trm.jpg")

  await ctx.send(file=discord.File("images/trm.jpg"))
  channel=client.get_channel(839596400149004328)

  date_time=now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  embed=discord.Embed(title= f"{ctx.author} has used the president command at {dt_string}!",colour=discord.Colour.red())
  
  embed.add_field(name="message sent:", value =f"k.president! {user}", inline=True)
  await channel.send(embed=embed)

@client.command()
async def message(ctx, *, message = "Didn't provide a message!"):
  channel=client.get_channel(840001430273916959)
  embed=discord.Embed(title='Incoming message', description=(message))
  await channel.send (embed=embed)
  await ctx.send(f"message `{message}` sent!")






############################################





@client.command(alieses=["nowon", "no1"])
async def noone(ctx, user: discord.Member = None):
  if user == None:
    user=ctx.author
    
  trump=Image.open("images/no one.png")
  
  asset=user.avatar_url_as(size=128)
    
  data=BytesIO(await asset.read())
  
  pfp=Image.open(data)
  
  pfp=pfp.resize((175, 172))  #289 173#

  trump.paste( pfp, (289, 173))
  trump.save("images/no one save.png")

  await ctx.send(file=discord.File("images/no one save.png"))
  channel=client.get_channel(839596400149004328)

  date_time=now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  embed=discord.Embed(title= f"{ctx.author} has used the no one meme command at {dt_string}!",colour=discord.Colour.red())
  
  embed.add_field(name="message sent:", value =f"k.president! {user}", inline=True)
  await channel.send(embed=embed)


@commands.command()
async def mus(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()

@client.command()
async def dog(ctx):
    rdog=random.randint(1,1000)
    embed=discord.Embed(title='Dog!')
    embed.set_image(url=f'https://placedog.net/{rdog}')
    await ctx.send(embed=embed)
    channel=client.get_channel(839596400149004328)
    date_time=now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    embed=discord.Embed(title= f"{ctx.author} has used the dog command at {dt_string}!",colour=discord.Colour.red())
  
    embed.add_field(name="message sent:", value =f"k.dog!", inline=True)
    await channel.send(embed=embed)
    embed=discord.Embed




@client.command()
async def rrn(ctx, num = 10):
    rrnum=random.randint(1, (num))
    embed=discord.Embed(title='Random number!', description=f'Your number is: {rrnum}!')
    await ctx.send(embed=embed)










@client.command()
async def aaa(ctx):
    rdog=random.randint(1,1000)
    embed=discord.Embed(title='Neko!')
    embed.set_image(url=f'https://placedog.net/{rdog}')
    await ctx.send(embed=embed)













@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)
  

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)
    if reason !=None:
        print("none")
    else:
        print("reason", (reason))



@client.command()
async def hug(ctx, *, user : discord.Member):
  rhug=random.choice(['https://media.tenor.com/images/eed8d1a51f647b4be696879a0ad6f1f1/tenor.gif', 'https://media.tenor.com/images/efb9895b66039cc344de289f14861047/tenor.gif'])
  embed=discord.Embed(title=f"{ctx.author} hugs {user}!", color=discord.Color.red())
  embed.set_image(url=(rhug))
  embed.set_footer(text="awwww cute")
  await ctx.send (embed=embed)

@client.command()
async def pingu(ctx):
    await ctx.send (f"User: ")






@client.command()
async def text(ctx, *, text = 'HMMM... SUS-'):
  img=Image.open("images/aa.PNG")

  draw=ImageDraw.Draw(img)
  font=ImageFont.truetype("fonts/font.otf", 24)
 # nfont=ImageFont.truetype("nfont.otf", 26)

  draw.text((100,45), text, (248,248,255), font=font)
 # draw.uname((100,50), text, (248,248,255), font=nfont)

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
  




@client.command(aliases=["randomnum", "rn"])
async def randomnumber(ctx):
  numer=random.randint(1,100)
  embed=discord.Embed(title= f"Your number is {numer}!",colour=discord.Colour.red())
  await ctx.send(embed=embed)
  channel=client.get_channel(839596400149004328)
  embed=discord.Embed(title=(f"{ctx.author}  has just used the command:"), description=f'{ctx}')
  await channel.send(embed=embed)




  


@client.command()
async def pain(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("http://aws.random.cat/meow") as r:
            data=await r.json()

            embed=discord.Embed(title=hug)
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
  
  
  
  





#@client.command(aliases=["howgay", "gayrate"])
#async def rategay(ctx):
#  rgay=random.randint(1,100)
 # embed=discord.Embed(title=f"you are {rgay}% gay.", color= discord.Color.red())
 # embed.set_image(gayflag)
#  await ctx.send(embed=embed)



@client.command()
async def susrate(ctx, user : discord.Member):
  susnum=random.randint(1,100)
  embed=discord.Embed(title='Sus rating!', description=f'{user} is {susnum}% sus!', color=discord.Color.red())
  await ctx.send(embed=embed)




@client.command(aliases=["say", "mimic"])
async def repeat(ctx, *, message):
  await ctx.send(message)
 

@client.command(aliases=["me", "myname", "mu"])
async def username(ctx):
  await ctx.send(ctx.author)





@client.command(aliases=["quote"])
async def script(ctx, *args):
  await ctx.send(args)





###spare cmd###
@client.command(aliases=["qss"])
async def nfk(ctx):
  await ctx.send("You are {gperc}% gay.")













###run client###

client.run(os.getenv('token'))