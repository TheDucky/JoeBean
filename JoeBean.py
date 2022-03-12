import requests
import discord
import os
from dotenv import load_dotenv
from time import time 

start = int(time() * 1000)
global snips
global depTime

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
    return(depTime)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    #check bot and server status
    #                           #
    #    STILL WORKING ON IT    #
    #############################

    # say hello!
    if msg.startswith('$hello'):
        await message.channel.send('Well hello there :)')

    # output a simple print statement 
    if msg.startswith('$simple-print'):
        snips = loadAPI()
        sp = snips["simple_print"][0]["snip"]
        await message.channel.send('```java\n' + sp + '\n```')

    # switch case and its example 
    if msg.startswith('$switch-case'):
        snips = loadAPI()
        sc = snips["switch_case"][0]["snip"]
        await message.channel.send('```java\n' + sc + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            scex = snips["switch_case"][0]["example"]
            await message.channel.send('```java\n' + scex + '\n```')

    # do while and its example
    if msg.startswith('$do-while'):
        snips = loadAPI()
        dw = snips["do_while"][0]["snip"]
        await message.channel.send('```java\n' + dw + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            dwex = snips["do_while"][0]["example"]
            await message.channel.send('```java\n' + dwex + '\n```')

    # if else and its example
    if msg.startswith('$if-else'):
        snips = loadAPI()
        ie = snips["if_else"][0]["snip"]
        await message.channel.send('```java\n' + ie + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            ieex = snips["if_else"][0]["example"]
            await message.channel.send('```java\n' + ieex + '\n```')
    
    # for loop and its example
    if msg.startswith('$for-loop'):
        snips = loadAPI()
        fl = snips["for_loop"][0]["snip"]
        await message.channel.send('```java\n' + fl + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            flex = snips["for_loop"][0]["example"]
            await message.channel.send('```java\n' + flex + '\n```')

    # while loop and its example
    if msg.startswith('$while-loop'):
        snips = loadAPI()
        wl = snips["while_loop"][0]["snip"]
        await message.channel.send('```java\n' + wl + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            wlex = snips["while_loop"][0]["example"]
            await message.channel.send('```java\n' + wlex + '\n```')

    # help embed
    if message.content.startswith('$help'):
        help = discord.Embed(title="Help is here", color=0x964B00)
        help.add_field(name="List of Commands", value="```-------------- \n$status \n$hello \n$simple-print \n$switch-case \n$do-while \n$if-else \n$for-loop \n$while-loop\n--------------\n```", inline=False)
        await message.channel.send(embed=help)

client.run(os.getenv('TOKEN'))