import requests
import discord
import os
from dotenv import load_dotenv
from time import time 

start = int(time() * 1000)

load_dotenv()
token = my_id = os.getenv("TOEKN") # paste your client id here
client = discord.Client()

def loadAPI():
    raw = requests.get('https://theducky.github.io/jSnip-API/API/jSnip.json')
    snips = raw.json()
    return(snips)

@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    stop = int(time() * 1000)
    depTime = (stop - start)/1000
    print('In: {0}s'.format(depTime))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msgs = message.content

    if msgs.startswith('$hello'):
        await message.channel.send('Well hello there :)')

    if msgs.startswith('$simple-print'):
        snips = loadAPI()
        sp = snips["simple_print"][0]["snip"]
        await message.channel.send('```java\n' + sp + '\n```')

client.run(os.getenv('TOKEN'))

def current_milli_time():
    return round(time.time() * 1000)