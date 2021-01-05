from twitchbot import Message, Mod

class MyMod(Mod):
    name = 'mymod'

    # async def loaded(self):
    #     print("mymod loaded *****")

    # async def on_privmsg_received(self, msg: Message):
    #     if 'hello' in msg.content:
    #         await msg.reply(f'hello {msg.author}!')
    
    # async def on_whisper_received(self, msg: Message):
    #     """
    #     triggered when a user sends the bot a whisper
    #     """
    #     if 'hi' in msg.content:
    #         # print('responding to whisper')
    #         await msg.reply(f'whisper received!', whisper=True)

    #async def on_user_join(self, user: str, channel: Channel):
    #    await msg.reply(f'Welcome to the channel {user}')

    # async def on_connected(self):
    #     """
    #     triggered when the bot connects to all the channels specified in the config file
    #     """
    #     await msg.reply('Reporting for duty!')