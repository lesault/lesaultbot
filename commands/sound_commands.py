from twitchbot import Command, SubCommand
from playsound import playsound

# @Command('gbu')
# async def cmd_function(msg, *args):
#     allowed_users = {'lesault'}
#     if msg.author in allowed_users:
#         playsound('sounds\GBUGLY Whistle.mp3', block=False)

@Command('splay', permission='admin')
async def cmd_splay(msg, *args):
    await msg.reply(' '.join(args))


# we pass the parent command as the first parameter   
@SubCommand(cmd_splay, 'bell')
async def cmd_splay_motd(msg, *args):
    playsound('sounds/front-desk-bell.mp3', block=False)
    
@SubCommand(cmd_splay, 'gbu')
async def cmd_splay_gbu(msg, *args):
    playsound('sounds/GBUGLY Whistle.mp3', block=False)

@SubCommand(cmd_splay, 'hb')
async def cmd_splay_hb(msg, *args):
    playsound('sounds/Heart_Beat.mp3', block=False)