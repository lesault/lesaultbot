from twitchbot import Command, CommandContext, InvalidArgumentsError, event_handler, Event, Channel

# Most of these commands come from lisareina's code - I need to customise them for lesaultbot!
# Take a look at the cool stuff they've done at https://github.com/lisareina/robotrei

# event handlers
# user joins - prints in run
@event_handler(Event.on_user_join)
async def on_user_join(user: str, channel: Channel):
    print(f'{user} joined')


# # maybe remove this bc it hurts my feelings
# @event_handler(Event.on_user_part)
# async def on_user_part(user: str, channel: Channel):
#     print(f'{user} left')


# # subscriptions
# @event_handler(Event.on_channel_subscription)
# async def on_channel_subscription(subscriber: str, channel: Channel, msg: Message):
#     await channel.send_message(f'omg @{subscriber} did something very cool. thank u.')


# # will be updated - follows
# @event_handler(Event.on_privmsg_received)
# async def on_privmsg_received(msg: Message):
#     allowed_users = {'streamlabs'}
#     if 'Thank you for following' in msg.content and msg.author in allowed_users:
#         await msg.reply('yes yes thank u for following! <3 i am the !bot of this channel')


# # bits
# @event_handler(Event.on_bits_donated)
# async def on_bits_donated(self, msg: Message, bits: int):
#     await msg.reply('thank you for cheering')


# misc

@Command('me', permission='me') 
async def cmd_function(msg, *args):
    await msg.reply(f'you exist {msg.mention}')

@Command('theend', permission='admin')
async def cmd_function(msg, *args):
    await msg.reply('Thank you for watching!!! Please give me a follow!')

@Command('discord', permission='admin')
async def cmd_function(msg, *args):
    await msg.reply('You can join my Discord at https://discord.gg/bWcNAyk')

@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply(
        'I have no schedule - I stream infrequently but that may change if I get some followers!')

@Command('tip')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention}, You can tip to lesault using this link https://StreamElements.com/lesault/tip')

# basics

@Command('bye')
async def cmd_function(msg, *args):
    await msg.reply(f'see u {msg.mention}, thanks for stopping by!')


@Command('brb', permission='admin')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} will be back soon!!')


# practical
@Command('sound', aliases=['loud', 'quiet'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lesault something is wrong with the sound')


@Command('muted', aliases=['m', 'mic'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lesault u are muted')


@Command('streamershoutout', aliases=['streamer', 'ss'], permission='admin')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'Shoutout to @{msg.mentions[0]} - check out their stream!')

@Command('snowball', aliases=['sb'],
        syntax='@<target>',
         help='throws a snowball at <target>')
async def cmd_function(msg, *args):
    if len(args) != 1:
        raise InvalidArgumentsError(reason='incorrect arguments arguments', cmd=cmd_function)
    target = args[0].lstrip('@')

    if not msg.mentions:
        raise InvalidArgumentsError(reason=f'no viewer found by the name "{(msg.mentions or args)[0]}"')

    print(msg.mentions)
    await msg.reply(f'{msg.mention} throws a snowball right in {args[0]}\'s face!')

@Command('pyramid', syntax='<num> <icon>',
         help='makes an icon pyramid of base <num> from <icon>', permission='admin')
async def cmd_function(msg, *args):
    if len(args) != 2:
        raise InvalidArgumentsError(reason='incorrect arguments arguments', cmd=cmd_function)
    i = 1 # number of <icon> for this row
    while i <= int(args[0]):
        await msg.reply(f'{args[1]} ' * i)
        i += 1

@Command('freeze', syntax='<target>',
         help='makes the bot ignore a user', permission='admin')
async def cmd_freeze(msg, *args):
    frozen_users = []
    with open('configs/frozen_users.txt', 'r') as f:
        for line in f:
	        frozen_users.append(line.strip('\n'))

    print('Testing Freeze')
    target = args[0].lstrip('@')
    frozen_users.append(target)
    await msg.reply(f'@{target} - you have been frozen')
    await msg.reply(f'Frozen users are: {frozen_users}')


# about

# bot feedbackdatabase
# @Command('goodbot', aliases=['goodrobot', 'good'])
# async def cmd_function(msg, *args):
#     await msg.reply(f'awww thank u {msg.mention} i am glad u like me')


# @Command('badbot', aliases=['badrobot', 'bad'])
# async def cmd_function(msg, *args):
#     await msg.reply(f'wow..... {msg.mention} i have feelings too you know... u try being a bot.... its not so easy')
#     # it would add a point or something????? into the database


# @Command('sorry')
# async def cmd_function(msg, *args):
#     await msg.reply(f'hmmm i dont know if i forgive you... robots never forgive or forget')


# @Command('die')
# async def cmd_function(msg, *args):
#     await msg.reply('oh wow... u big meanie.... speechlesssss')


@Command('bot', aliases=['framework', 'twitchbot'])
async def cmd_function(msg, *args):
    await msg.reply(f'I\'m built using https://github.com/sharkbound/PythonTwitchBotFramework')

@Command('say', permission='admin', )
async def cmd_say(msg, *args):
    await msg.reply(' '.join(args))

@Command('twitchcmd', permission='admin', )
async def cmd_twitchcmd(msg, *args):
    await msg.send_command(' '.join(args))
    