#https://github.com/sixhobbits/python-telegram-tutorial/blob/master/part1/echobot.py
import json
import requests
import time
import urllib
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup



TOKEN = '1799839165:AAGHhy1cH0pd4Ey-jNqEqSdj6HtgeEUSlT4'
URL = "https://api.telegram.org/bot1799839165:AAGHhy1cH0pd4Ey-jNqEqSdj6HtgeEUSlT4/"
bot = telepot.Bot(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def reply_mes(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)
        if text == "/start":
            bot.sendMessage(
                chat, text="Hi there, let's start our simple assessment now."
            )
            assess(text, chat) #run the assessment function 
        elif text == "/learn":
            bot.sendMessage(
                chat,
                "Learn more at https://amyphenjati.github.io/team_asia/learn_more.html",
            )    


def assess(last_text, chat_id):
    i = 0
    yes_count = 0
    no_count = 0
    with open("text/questions.txt") as questions:
        lines = [line.rstrip("\n") for line in questions]
        while i < len(lines):
            quest = lines[i]
            i += 1
            mark_up = ReplyKeyboardMarkup(
                keyboard=[["Yes"], ["No"]], one_time_keyboard=True
            )
            bot.sendMessage(chat_id, text=quest, reply_markup=mark_up)
            if last_text == "Yes":
                yes_count += 1
            elif last_text == "No":
                no_count += 1
            else:
                bot.sendMessage(chat_id, text="please start over")
        bot.sendMessage(chat_id, text=yes_count)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            reply_mes(updates)
        # time.sleep(0.5)


if __name__ == '__main__':
    main()