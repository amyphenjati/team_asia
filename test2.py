#amy's random test on telepot


# import sys
# import time
# import telepot #import teleport module
# from pprint import pprint
# from telepot.loop import MessageLoop

# bot = telepot.Bot("1799839165:AAGHhy1cH0pd4Ey-jNqEqSdj6HtgeEUSlT4") 

# print(bot.getMe())
# respond = bot.getUpdates()
# pprint(respond)

# def handle(msg):
#     pprint(msg)

# print(MessageLoop(bot, handle).run_as_thread())

# bot.sendMessage(1702405405, 'im trying out telepot!')

# import time
# import telepot
# from telepot.loop import MessageLoop

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id)

#     if content_type == 'text':
#         bot.sendMessage(chat_id, msg['text'])

# TOKEN = '1799839165:AAGHhy1cH0pd4Ey-jNqEqSdj6HtgeEUSlT4'

# bot = telepot.Bot(TOKEN)
# MessageLoop(bot, handle).run_as_thread()
# print ('Listening ...')

# # Keep the program running.
# while 1:
#     time.sleep(10)

import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if msg['text'] == '/start':
        bot.sendMessage(chat_id, 'Lets begin your assessment')
    elif msg['text'] == '/learn':
        bot.sendMessage(chat_id, 'Learn more at https://amyphenjati.github.io/team_asia/learn_more.html')

TOKEN = '1799839165:AAGHhy1cH0pd4Ey-jNqEqSdj6HtgeEUSlT4'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)