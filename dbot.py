import discord, os
from dbot_logic import *
import random

print(os.listdir('images'))

weights = {
    'mem1.jpg': 0.45,
    'mem2.jpg': 0.3,
    'mem3.jpg': 0.2,
    'DisMeme.jpg': 0.04,
    'DisMeme2.jpg': 0.01,
    }

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#Запуск бота
@client.event
async def on_ready():
    print(f"I'm logged as {client.user}")
    print('Write "!help" in a chat with a bot to get a list of commands.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #команды
    if message.content.startswith("!hello") or message.content.startswith("!hi") or message.content.startswith("!привет"):
        await message.channel.send("Здорова чел")

    elif message.content.startswith('!bye') or message.content.startswith("!пока"):
        await message.channel.send("Ладно, покеда")

    elif message.content.startswith('!pass') or message.content.startswith('!пароль'):
        await message.channel.send(gen_pass(10))

    elif message.content.startswith('!emoji'):
        await message.channel.send(gen_emodji())

    if message.content.startswith("!help") or message.content.startswith('!помощь'):
        await message.channel.send(get_help())

    elif message.content.startswith('!magic') or message.content.startswith('!магия'):
        if len(message.content) > len("!magic .?") and message.content.endswith('?'):
            await message.channel.send(magic_ball())
        else:
            await message.channel.send("Извини уж, но это не вопрос")

    elif message.content.startswith("!memes") or message.content.startswith('!мемы'):
        img_name = random.choice(os.listdir('images'))
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

    elif message.content.startswith("!memerandom") or message.content.startswith('!мемрандом'):
        img_name = random.choices(list(weights.keys()), weights=list(weights.values()), k=1)[0]
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

    elif message.content.startswith("!duck") or message.content.startswith('!утка'):
        image_url = get_duck_image_url()
        await message.channel.send(image_url)
    #else:
        #await message.channel.send(message.content)

#paste your token here
client.run("Paste YOUR token here")