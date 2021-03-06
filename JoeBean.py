#! /bin/python3

from pyston import PystonClient, File
import requests
import discord
import os
from datetime import datetime
from dotenv import load_dotenv
from time import time 

start = int(time() * 1000)
global snips
global depTime
now = datetime.now()

load_dotenv()
client = discord.Client()

def loadAPI():
    raw = requests.get('https://theducky.github.io/jSnip-API/API/jSnip.json')
    snips = raw.json()
    return(snips)

snips = loadAPI()

@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    stop = int(time() * 1000)
    depTime = (stop - start)/1000
    logDate = now.strftime("%d/%m/%Y %H:%M:%S")
    pid = os.popen("ps -ef | grep 'python3 -u JoeBean.py' | awk 'NR==1{print $2}'")
    print("At: {0}".format(logDate))
    print('In: {0}s'.format(depTime))
    print('killSwitch: {0}'.format(pid.read()))
    print("-------------------------------------------")
    return(depTime)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    global snips

    #check bot and server status
    if msg.startswith('$status'):
        name = message.author.mention
        await message.channel.send(name)
        print(name)
        if name == '<@775405500028289044>':
            await message.channel.send("Only you can use this command")
        
        else:
            await message.channel.send("sorry buddy, you dont have access to this command")

    # say hello!
    if msg.startswith('$hello'):
        await message.channel.send('Well hello there :)')
    
    # output a simple print statement 
    if msg.startswith('$simple-print'):
        sp = snips["simple_print"][0]["snip"]
        await message.channel.send('```java\n' + sp + '\n```')

    # switch case and its example 
    if msg.startswith('$switch-case'):
        sc = snips["switch_case"][0]["snip"]
        await message.channel.send('```java\n' + sc + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            scex = snips["switch_case"][0]["example"]
            await message.channel.send('```java\n' + scex + '\n```')

    # do while and its example
    if msg.startswith('$do-while'):
        dw = snips["do_while"][0]["snip"]
        await message.channel.send('```java\n' + dw + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            dwex = snips["do_while"][0]["example"]
            await message.channel.send('```java\n' + dwex + '\n```')

    # if else and its example
    if msg.startswith('$if-else'):
        ie = snips["if_else"][0]["snip"]
        await message.channel.send('```java\n' + ie + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            ieex = snips["if_else"][0]["example"]
            await message.channel.send('```java\n' + ieex + '\n```')
    
    # for loop and its example
    if msg.startswith('$for-loop'):
        fl = snips["for_loop"][0]["snip"]
        await message.channel.send('```java\n' + fl + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            flex = snips["for_loop"][0]["example"]
            await message.channel.send('```java\n' + flex + '\n```')

    # while loop and its example
    if msg.startswith('$while-loop'):
        wl = snips["while_loop"][0]["snip"]
        await message.channel.send('```java\n' + wl + '\n```')
        await message.channel.send('If you want an example add `& example` at the end of the command')

        if " & example" in msg:
            wlex = snips["while_loop"][0]["example"]
            await message.channel.send('```java\n' + wlex + '\n```')
    
    # show them how to format the code.
    if msg.startswith('$howto-run'):
        await message.channel.send('**Please format your code like so:**\n$run-code\n\```java\n//Code block\n\```\n **If you fail to format your code in this manner the code will not run**')

    # run java code
    if msg.startswith('$run-code'):
        codeArr = msg.split()
        del codeArr[0:2]
        codeArr.pop()
        code = ' '.join(codeArr)

        piston = PystonClient()
        output = await piston.execute("java", [File(code)])
        await message.channel.send('Java OUTPUT for: {0}'.format(message.author.mention))
        await message.channel.send('```\n{0}\n```'.format(output))

        # old code.
        #try:
        #    output = os.popen('java Main.java')
        #    await message.channel.send('Java OUTPUT using version:`openjdk 11.0.14` for: {0}'.format(message.author.mention))
        #    await message.channel.send('```\n{0}\n```'.format(output.read()))
        #except:
        #    await message.channel.send('There were a few errors. Check them and try again')

    # help embed
    if message.content.startswith('$help'):
        help = discord.Embed(title="Help is here", color=0x964B00)
        help.add_field(name="List of Commands", value="```-------------- \n$status \n$hello \n$simple-print \n$switch-case \n$do-while \n$if-else \n$for-loop \n$while-loop \n$run-code \n--------------\n```", inline=False)
        await message.channel.send(embed=help)
    
    # update snippets command
    if message.content.startswith('$update'):
        snips = loadAPI()
        await message.channel.send('All code snippets is updated')

    # dont ping us
    if '<@!775405500028289044>' in message.content:
        await message.channel.send('AYO {0}, DONT PING HIM!'.format(message.author.mention))

    if '<@!756742321151934504>' in message.content:
        await message.channel.send('AYO {0}, DONT PING HIM!'.format(message.author.mention))

client.run(os.getenv('TOKEN'))
