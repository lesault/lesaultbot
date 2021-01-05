from twitchbot import Command
import json
from urllib.request import urlopen
import asyncio

# jokes
@Command('joke', cooldown=60)
async def cmd_function(msg, *args):
    # &contains=test
    if len(args) > 0:
        subject = '&contains=' + args[0].replace(' ', '%20')
    else: 
        subject=''
    joke = json.loads(urlopen('https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,racist,sexist,explicit' + subject).read())
    if joke['error'] == False:
        if joke['type'] == 'single':
            message = joke['joke'].split('\n')
            for line in message:
                await msg.reply(line)
        elif joke['type'] == 'twopart':
            setup = joke['setup'].split('\n')
            delivery = joke['delivery'].split('\n')
            for line in setup:
                await msg.reply(line)
            await asyncio.sleep(3)
            for line in delivery:
                await msg.reply(line)
    else:
        await msg.reply('I\'ve had a sense of humour failure...')