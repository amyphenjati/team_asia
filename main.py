TOKEN = "1733137548:AAEMqq-UKBhfVcLD-ReXzHtQW49eJmIoEBA" # personal consultant bot API key

"""
Telegram bot for basic mental health check that 
generates 10 yes/no poll questions and 
counts yes answers to recommend users on menthal health issues. 
"""

# import relevant libraries 
# first install telegram in command prompt (pip install telegram-python-bot)
import logging
from telegram import *
from telegram.ext import *

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO) # format information storage configuration
logger = logging.getLogger(__name__)


def start(update: Update, _: CallbackContext) -> None:
    """Function replies users with a greeting message after users sends /start"""
    update.message.reply_text(f"Hello, I am your personal consultant. Your mental health is very important, so let check in on how you are doing! We will now be asking you 10 yes/no questions. Type /poll to continue or /help to learn more.")


def poll(update: Update, context: CallbackContext) -> None:
    """Sends a predefined poll of 10 yes/no questions for users to answer after typing /poll on telegram"""
    question_list = [
        "1. I have lost interest in things I used to like to do.",
        "2. I feel hopeless about my future.",
        "3. I find it more difficult than it should be to make decisions.",
        "4. I feel sluggish and often get tired for no reason.",
        "5. I am gaining or losing weight without intending to.",
        "6. I feel helpless to make changes I’d like to make in my life.",
        "7. I am sleeping too much, or too little.",
        "8. I often feel unhappy or sad, or easily cry.",
        "9. I easily become irritable or anxious.",
        "10. I think about dying or killing myself.",
    ]
    questions = ["Yes", "No"] # answer options for users
    for i in range(10): # bot will send all 10 questions with yes/no options separately 
        message = context.bot.send_poll(
            update.effective_chat.id,
            question_list[i],
            questions,
            is_anonymous=False,
            allows_multiple_answers=False,
        )
        # Save some info about the poll the bot_data for later use in receive_poll_answer
        payload = {
            message.poll.id: {
                "questions": questions,
                "message_id": message.message_id,
                "chat_id": update.effective_chat.id,
                "answers": 0,
            }
        }
        context.bot_data.update(payload) 

all_data = {} # new dictionary collecting all data
total_num_ans = {} # dictionary counting total number of answers

def receive_poll_answer(update: Update, context: CallbackContext) -> None:
    """Summarize a users poll vote and generates a concluding message depending on number of yes answers"""
    answer = update.poll_answer
    # print(answer)
    poll_id = answer.poll_id
    try:
        questions = context.bot_data[poll_id]["questions"] # this means this poll answer update is from an old poll, we can't do our answering then
    except KeyError:
        return
    selected_options = answer.option_ids 
    answer_string = ""
    
    global all_data # globalize dictionary to be used anywhere
    global total_num_ans # globalize dictionary to be used anywhere
    
    if questions[selected_options[0]] == "Yes": # count number of yes answers
        all_data[answer["user"]["id"]] = all_data.get(answer["user"]["id"], 0) + 1 # increase count by 1 if answered yes
    total_num_ans[answer["user"]["id"]] = total_num_ans.get(answer["user"]["id"], 0) + 1 # increase total number of questions answers by 1 
    
    if answer["user"]["id"] not in all_data: # if user answers all no's
        all_data[answer["user"]["id"]] = 0 # indicates 0 yes answers

    if (total_num_ans[answer["user"]["id"]] == 10 and all_data[answer["user"]["id"]] / 10.0 > 0.3): # if all 10 questions are answered and user answers more than 3 yes's
        context.bot.send_message(
            context.bot_data[poll_id]["chat_id"],
            f"All done, {update.effective_user.mention_html()}. You have answered yes {all_data[answer['user']['id']]} questions. If you have felt this way most every day for several weeks, you may be experiencing depression and should seek a full assessment by a psychiatrist, mental health counselor or other health care professional. If you answered yes to question 10, you should seek help immediately, regardless of your answer to any other questions.Learn more at https://amyphenjati.github.io/team_asia/learn_more.html",
            parse_mode=ParseMode.HTML,
        )
    elif total_num_ans[answer["user"]["id"]] == 10: # for cases where users answered less than 3 yes's
        context.bot.send_message(
            context.bot_data[poll_id]["chat_id"],
            f"{update.effective_user.mention_html()}, you are problably stressed. Don't worry, try meditating! BUT if you answered 'yes' to question 10, you should seek help immediately, regardless of your answer to any other questions.",
            parse_mode=ParseMode.HTML,
        )


def help_handler(update: Update, _: CallbackContext) -> None:
    """Function replies users with message linking to a html page for more information when users type /help."""
    update.message.reply_text( "Learn more at https://amyphenjati.github.io/team_asia/learn_more.html")


def main() -> None:
    # Create the Updater and pass it bot's token.
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("poll", poll))
    dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
    dispatcher.add_handler(CommandHandler("help", help_handler))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()