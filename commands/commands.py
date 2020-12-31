from twitchbot import Command

import datetime

# Most of these commands come from lisareina's code - I need to customise them for lesaultbot!
# Take a look at the cool stuff they've done at https://github.com/lisareina/robotrei

# misc

@Command('me')
async def cmd_function(msg, *args):
    await msg.reply(f'you exist {msg.mention}')


@Command('tea')
async def cmd_function(msg, *args):
    await msg.reply('Yes please! 1 sugar and a shot of whisky...')


@Command('theend')
async def cmd_function(msg, *args):
    allowed_users = {'lesault'}
    if msg.author in allowed_users:
        await msg.reply(
            'thank u all for watching!!! pls follow me!!! also come to my discord and see u tomorrow!!! <3 https://discord.gg/bWcNAyk')


@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply(
        'No schedule - I stream infrequenly but that may change if I get some followers!')


# basics

@Command('bye')
async def cmd_function(msg, *args):
    await msg.reply(f'see u {msg.mention}, thanks for stopping by!')


@Command('brb')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} will be back soon!!')


@Command('lurk')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} hides in the shadows and watches.')


# @Command('time', aliases=['timezone'])
# async def cmd_function(msg, *args):
#     await msg.reply(
#         f'time is  a social construct but here u go, it is: {(datetime.datetime.now()).strftime("%H:%M, %A %d/%m")}... gmt+1 babyy')


# practical
@Command('sound', aliases=['loud', 'quiet'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lesault something is wrong with the sound')


@Command('muted', aliases=['m', 'mic'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lesault u are muted')


# @Command('posture')
# async def cmd_function(msg, *args):
#     await msg.reply(
#         f'u gotta use channel points to make me not sit like a pretzel... but just this once ill sit up straight anyway')


# @Command('hydrate')
# async def cmd_function(msg, *args):
#     await msg.reply(
#         f'u gotta use channel points to make me drinkkk... but just this once ill take a sip since its u {msg.mention}')


# @Command('hug')
# async def cmd_function(msg, *args):
#     print(msg.mentions)
#     await msg.reply(f'u have been hugged @{msg.mentions[0]}')


# @Command('thankyou', aliases=['thnx', 'ty'])
# async def cmd_function(msg, *args):
#     print(msg.mentions)
#     await msg.reply(f' oooo @{msg.mentions[0]} thank u!!! <3 i love u')


@Command('streamershoutout', aliases=['streamer', 'ss'])
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'shoutout to @{msg.mentions[0]} who is also a streamer!! go follow them')


# about

# bot feedbackdatabase
# @Command('goodbot', aliases=['goodrobot', 'good'])
# async def cmd_function(msg, *args):
#     await msg.reply(f'awww thank u {msg.mention} i am glad u like me')


# @Command('badbot', aliases=['badrobot', 'bad'])
# async def cmd_function(msg, *args):
#     await msg.reply(f'wow..... {msg.mention} i have feelings too you know... u try being a bot.... its not so easy')
#     # it would add a point or something????? into the database


@Command('bot')
async def cmd_function(msg, *args):
    await msg.reply(
        'i am not a bot i am a robot.... use !robot pls. but fine fine... i am a twitchbot, made in python, to see my insides use !github')


@Command('sorry')
async def cmd_function(msg, *args):
    await msg.reply(f'hmmm i dont know if i forgive you... robots never forgive or forget')


@Command('die')
async def cmd_function(msg, *args):
    await msg.reply('oh wow... u big meanie.... speechlesssss')


@Command('daddy', aliases=['framework', 'twitchbot'])
async def cmd_function(msg, *args):
    await msg.reply(f'my daddy is https://github.com/sharkbound/PythonTwitchBotFramework')


@Command('say')
async def cmd_say(msg, *args):
    allowed_users = {'lesault'}
    if msg.author in allowed_users:
        await msg.reply(' '.join(args))