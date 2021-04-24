# i = 0
# yes_count = 0
# no_count = 0
# with open('text/questions.txt') as questions:
#     lines = [line.rstrip('\n') for line in questions]
#     while i < len(lines):
#         quest = lines[i]
#         i+=1
#         print(quest)
#         x = input()
#         if x == 'yes':
#             yes_count +=1
#         elif x == 'no':
#             no_count +=1
#         else:
#             print('please start over')
#             break

#print('yes_count', yes_count)
#print('no_count', no_count)
# print(lines[1])

###############################################################
# API_KEY = '1733137548:AAEMqq-UKBhfVcLD-ReXzHtQW49eJmIoEBA'

# from telegram.ext import *

# def sample_responses(input_text):
#     user_message = str(input_text).lower()

#     if user_message in ("hello", "hi"):
#         return "We will now be asking you 10 yes/no questions to check in on how you are doing. Type OK to continue."
        
#     if user_message in ("ok", "okay"):
#         return "1. I have lost interest in things I used to like to do."

#     i = 0
#     yes_count = 0
#     no_count = 0

#     if user_answer in ("yes"):
#         yes_count += 1
#         return "2. I feel hopeless about my future."
#     if user_answer in ("no"):
#         no_count += 1
#         return "2. I feel hopeless about my future."
    
#     return "Sorry, I don't understand you."

# print("Bot started...")

# def start_command(update, context):
#     update.message.reply_text('Type hello/hi to get started!')

# def help_command(update, context):
#     update.message.reply_text('Learn more at https://amyphenjati.github.io/team_asia/learn_more.html')

# def handle_message(update, context):
#     text = str(update.message.text).lower() # receive text from user
#     response = sample_responses(text) # process text

#     update.message.reply_text(response) # puts it back out to the users

# def error(update, context):
#     print(f"Update {update} caused error {context.error}")

# def main():
#     updater = Updater(API_KEY, use_context= True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start_command))
#     dp.add_handler(CommandHandler("help", help_command))

#     dp.add_handler(MessageHandler(Filters.text, handle_message))

#     dp.add_error_handler(error)

#     updater.start_polling(0) # wait for 7 seconds for users to send something
#     updater.idle()

# main()

with open("text/questions.txt", 'r', encoding="utf-8") as file:
    new_list = file.read()
    new_list = [new_list.rstrip('\n') for line in new_list]

print(new_list)





