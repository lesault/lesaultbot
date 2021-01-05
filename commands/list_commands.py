from twitchbot import Command
import random


@Command('fortune')
async def cmd_function(msg, *args):
    await msg.reply(fortune_options(msg))


def fortune_options(msg):
    fortunes = ['You\'re being followed.  Cut out the hanky-panky for a few days.',
                'You are capable of planning your future.',
                'You have an unusual equipment for success.  Be sure to use it properly.',
                'Stay away from hurricanes for a while.',
                'Change your thoughts and you change your world.',
                'Your fly might be open (but don\'t check it just now).',
                'People are beginning to notice you.  Try dressing before you leave the house.',
                'Chicken Little was right.',
                'Increased knowledge will help you now.  Have mate\'s phone bugged.',
                'Afternoon very favorable for romance.  Try a single person for a change.',
                'You have many friends and very few living enemies.',
                'Try the Moo Shu Pork.  It is especially good today.',
                'Don\'t look now, but there is a multi-legged creature on your shoulder.',
                'You are wise, witty, and wonderful, but you spend too much time reading this sort of trash.',
                'You are the only person to ever get this message.',
                'You have an unusual magnetic personality.  Don\'t walk too close to metal objects which are not fastened down',
                'Don\'t tell any big lies today.  Small ones can be just as effective.']
    return random.choice(fortunes)


@Command('lurk')
async def cmd_function(msg, *args):
    await msg.reply(lurk_options(msg) + ' (lurking)')


def lurk_options(msg):
    lurk_messages = [f'{msg.author} hides in the shadows and watches silently.',
                     f'{msg.author} disappears in a puff of smoke.',
                     ]
    return random.choice(lurk_messages)