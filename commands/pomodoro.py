from twitchbot import Command, CommandContext, InvalidArgumentsError, event_handler, Event, Channel, Message
import asyncio
from playsound import playsound

pomo_clock = 'pomo_out.txt'
pomo_status = 'pomo_status.txt'
pomo_message = 'pomo_message.txt'
timer_increase_on_follow = 120
bits_exchangerate = 3 # 1 bit is ~$0.01 so 100 bits gets them 300 seconds (5  mins)
timer_instance = 0

@Command('pomo', syntax='<minutes> [status]', help='starts or changes a pomodoro timner to display on overlay', permission='Admin')
async def cmd_function(msg, *args):
    global timer_seconds
    global timer_instance
    this_timer_instance = timer_instance + 1
    timer_instance = this_timer_instance
    
    if not args:
        raise InvalidArgumentsError(reason='missing required arguments', cmd=cmd_pomo)
    
    timer_minutes=int(args[0])
    if len(args) == 2:
        status=args[1]

        with open(pomo_status, "w") as f:
            f.write(status)
    
    timer_seconds = timer_minutes * 60
    await msg.reply(f'Pomodoro timer counting down from {timer_minutes} minutes!')

    while (timer_seconds >= 0) and (this_timer_instance == timer_instance):
        mins, secs = divmod(timer_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        with open(pomo_clock, "w") as f:
            f.write(timer)
        await asyncio.sleep(1)
        timer_seconds -= 1
    
    if this_timer_instance == timer_instance:
        playsound('sounds/front-desk-bell.mp3', block=False)
        await msg.reply('Pomodoro timer finished!')
        timer_instance=0

# Testing changes to the timer on events - this is for on_join, should really do one for bits, subs, follows, tips instead.
# @event_handler(Event.on_user_join)
# async def on_user_join(user: str, channel: Channel):
#     global timer_seconds
#     global timer_instance
#     if timer_instance > 0: # if a pomo timer is running
#         await channel.send_message(f'{user} joined - increasing the timer by {timer_increase_on_follow} seconds!')
#         timer_seconds += timer_increase_on_follow

@event_handler(Event.on_bits_donated)
async def on_bits_donated(self, msg: Message, bits: int):
    """
    triggered when a bit donation is posted in chat
    """
    global timer_seconds
    global timer_instance
    if timer_instance > 0: # if a pomo timer is running
        await channel.send_message(f'{bits} donated while a Pomodoro is running! - increasing the timer by {int(bits * bits_exchangerate)} seconds!')
        timer_seconds += int(bits * bits_exchangerate)

@Command('pomomsg', syntax='<Message> use /n for newline.', help='sets a message on the Twitch overlay')
async def cmd_pomomsg(msg, *args):
    if len(args) == 0:
        raise InvalidArgumentsError('missing required arguments')
    
    print(' '.join(args).split('¬'))
    with open(pomo_message, "w") as f:
            f.writelines(s + '\n' for s in ' '.join(args).split('/n'))

    await msg.reply('Pomo message updated')
