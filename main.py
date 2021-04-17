import conf
import discord
from discord.ext import commands
import img_handler as imhl
import os

intents = discord.Intents.default()
intents.members = True



bot = commands.Bot(command_prefix="!", intents = intents)

channel = 825309119589122088
@bot.command(name="hello")
async def command_hello(ctx):
    global channel
    if ctx.channel.id == channel:
        msg = f'helo, F*ck marriot'
        await ctx.channel.send(msg)

@bot.command(name="repeat")
async def repeat(ctx):
    global channel
    if ctx.channel.id == channel:
        if ctx.message.content == "!repeat":
            await ctx.send(f'what?')
        else:
            await ctx.send(f'{ctx.message.content[7:]}')

@bot.command(name="about_me")
async def about_me(ctx):
    global channel
    if ctx.channel.id == channel:
        await ctx.channel.send(f'Your name is {ctx.message.author.name} \nYour id is {ctx.message.author.id}\n{"Your nickname is " + ctx.message.author.nick if ctx.message.author.nick != None else ""}')

@bot.command(name="get_channels")
async def get_channels(ctx):
    count = 1
    msg = ""
    global channel
    if ctx.channel.id == channel:
        for channel in ctx.guild.channels:
            msg += f'{count}. {channel} - {channel.id} \n'
            count += 1
    
        await ctx.channel.send(msg)
@bot.command(name="get_members")
async def get_members(ctx):
    msg = ''
    count = 1
    global channel
    if ctx.channel.id == channel:
        for member in ctx.guild.members:
              
              
            msg += f'{count}. {member} {"- " + member.nick if member.nick != None else ""} - {member.id}\n'
            count += 1
        await ctx.channel.send(msg)
@bot.command(name="get_member")
async def get_member(ctx, member:discord.Member=None ):
    msg = None
    global channel
    if ctx.channel.id == channel:
        if member:
            msg = f'Member {member.name} {"- " + member.nick if member.nick != None else ""} - {member.id}'

        if msg == None:
            msg = "ERROR"
        await ctx.channel.send(msg)
     
@bot.command(name="mk")
async def mk(ctx, f1:discord.Member=None, f2:discord.Member=bot.user):

    global channel
    if ctx.channel.id == channel:
        print(f1.avatar_url, f2.avatar_url)
        await imhl.vs_create(f1.avatar_url, f2.avatar_url)

        await ctx.channel.send(file = discord.File(os.path.join("./img/result.png")))



bot.run(conf.bot_token)