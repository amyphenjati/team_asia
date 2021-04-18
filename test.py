import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup

url = "https://api.telegram.org/bot1799839165:AAGHhy1cH0pd4Ey-jNqEqSdj6HtgeEUSlT4/"
token = "1799839165:AAGHhy1cH0pd4Ey-jNqEqSdj6HtgeEUSlT4"
bot = telepot.Bot(token)
bot.getMe()


def q_a(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    i = 0
    yes_count = 0
    no_count = 0
    if msg["text"] == "/start":
        bot.sendMessage(
            chat_id, text="Hi there, let's start our simple assessment now."
        )
        with open("text/questions.txt") as questions:
            lines = [line.rstrip("\n") for line in questions]
            while i < len(lines):
                quest = lines[i]
                i += 1
                mark_up = ReplyKeyboardMarkup(
                    keyboard=[["Yes"], ["No"]], one_time_keyboard=True
                )
                bot.sendMessage(chat_id, text=quest, reply_markup=mark_up)
                if msg["text"] == "Yes":
                    yes_count += 1
                elif msg["text"] == "Yes":
                    no_count += 1
                else:
                    bot.sendMessage(chat_id, text="please start over")
            bot.sendMessage(chat_id, text=yes_count)
    
    elif msg['text'] == '/learn':
        bot.sendMessage(chat_id, 'Learn more at https://amyphenjati.github.io/team_asia/learn_more.html')


bot = telepot.Bot(token)
MessageLoop(bot, q_a).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
