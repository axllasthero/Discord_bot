import conf
import discord
from discord.ext import commands


#intents = discord.Intents.default()
#intents.members = True
#
#client = discord.Client(intents=intents)
#
#
#
#
#@client.event
#async def on_message(message):
#    #<Message 
#    # id=825338292228718603 
#    # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
#    # type=<MessageType.default: 0> 
#    # author=<Member id=307383433036824579 name='dimaditriy' discriminator='1518' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>> 
#    #  flags=<MessageFlags value=0>>
#        
#    if message.author == client.user:
#        return 
#    
#
#    if message.author.bot:
#        return
#
#    if message.channel.id == 825309119589122088:
#        msg = None
# 
#        
#
#        if message.content == "/hello":
#            msg = f'Hello, {message.author.name}. I am {client.user.name}'
#        elif message.content == "/about_me":
#            msg = f'Your name is {message.author.name} \nYour id is {message.author.id}\n{"Your nickname is " + message.author.nick if message.author.nick != None else ""}\nAnd ur mom gay '
#        elif message.content.startswith('/repeat'):
#            msg = message.content.replace('/repeat', '')
#        elif message.content.startswith('/get_member'):
#            mem_id = message.content.replace('/get_member ', '')
#            if mem_id == '':
#                msg = f'Who?'
#            else:
#               #for member in message.guild.members:
#               #    if mem_id == member.id:
#               #        msg = f'Name = {member}'
#                
#                if mem_id.isdigit():
#                    msg = f'Name = {message.guild.get_member(int(mem_id))}'
#                    print(mem_id.strip())
#                else:
#                   msg = f'Name = {message.guild.get_member(mem_id)}' 
#        elif message.content.startswith('/get_channels'):
#            msg = ''
#            count = 1
#            for channel in client.get_all_channels():
#                
#                msg += f'{count}. {channel} - {channel.id} \n'
#                count += 1
#        elif message.content.startswith('/members'):
#            msg = ''
#            count = 1
#            for member in message.guild.members:
#                
#                
#                msg += f'{count}. {member} {"- " + member.nick if member.nick != None else ""} - {member.id}\n'
#                count += 1
#
#        elif message.content.startswith('/goto'):
#
#            message.channel.id = message.content.replace('/goto ', '')
#            msg = 'moved to new channel'
#            
#        await message.channel.send(msg)
#
#        
#
#
#client.run(conf.bot_token)
#


bot = commands.Bot(command_prefix="/")

@bot.command(name="hello")
async def command_hello(ctx, *args):
    message = " ".join(args)
    if ctx.channel.id == 825309119589122088:
        msg = f'F*ck marriot, less do some {message}'
        await ctx.channel.send(msg)

bot.run(conf.bot_token)