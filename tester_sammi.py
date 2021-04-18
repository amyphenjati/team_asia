token = '1611604660:AAFjP0uF2glArw2XGJz8yNQvbucISbVrv4E'
import telepot
from pprint import pprint
from telepot.loop import MessageLoop

bot = telepot.Bot(token)
print(bot.getMe())