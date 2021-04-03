import conf
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)




@client.event
async def on_message(message):
    #<Message 
    # id=825338292228718603 
    # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
    # type=<MessageType.default: 0> 
    # author=<Member id=307383433036824579 name='dimaditriy' discriminator='1518' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>> 
    #  flags=<MessageFlags value=0>>
        
    if message.author == client.user:
        return 
    

    if message.author.bot:
        return

    if message.channel.id == 825309119589122088:
        msg = None
        

        ctx = message.content.split(" ", maxsplit=1)
        if message.content == "/hello":
            msg = f'Hello, {message.author.name}. I am {client.user.name}'
        elif message.content == "/about_me":
            msg = f'Your name is {message.author.name} \nYour id is {message.author.id}\n{"Your nickname is " + message.author.nick if message.author.nick != None else ""}\nAnd ur mom gay '
        elif message.content.startswith('/repeat'):
            msg = message.content.replace('/repeat', '')
        elif message.content.startswith('/get_member'):
            mem_id = message.content.replace('/get_member', '')
            if mem_id == '':
                msg = f'Who?'
            else:
                msg = f'Name = {message.guild.get_member(825328952364761129)}'
                print(mem_id.strip())
        elif message.content.startswith('/members'):
            msg = ''
            count = 1
            for member in message.guild.members:
                
                
                msg += f'{count}. {member} {"- " + member.nick if member.nick != None else ""} - {member.id}\n'
                count += 1
        await message.channel.send(msg)

        


client.run(conf.bot_token)
