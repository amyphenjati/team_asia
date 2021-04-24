TOKEN = '1733137548:AAEMqq-UKBhfVcLD-ReXzHtQW49eJmIoEBA'

"""
Basic example for a bot that works with polls. Only 3 people are allowed to interact with each
poll/quiz the bot generates. The preview command generates a closed poll/quiz, exactly like the
one the user sends the bot
"""
import logging

from telegram import (
    Poll,
    ParseMode,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    PollAnswerHandler,
    PollHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, _: CallbackContext) -> None:
    """Inform user about what this bot can do"""
    update.message.reply_text(
        'Please select /poll to get a Poll, /quiz to get a Quiz or /preview'
        ' to generate a preview for your poll'
    )

def poll(update: Update, context: CallbackContext) -> None:
    """Sends a predefined poll"""
    question_list = ["1. I have lost interest in things I used to like to do.", 
    "2. I feel hopeless about my future.",
    "3. I find it more difficult than it should be to make decisions.",
    "4. I feel sluggish and often get tired for no reason.",
    "5. I am gaining or losing weight without intending to.",
    "6. I feel helpless to make changes I’d like to make in my life.",
    "7. I am sleeping too much, or too little.",
    "8. I often feel unhappy or sad, or easily cry.",
    "9. I easily become irritable or anxious.",
    "10. I think about dying or killing myself."]
    questions = ["Yes", "No"]
    for i in range(10):
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

all_data = {}
total_num_ans = {}
def receive_poll_answer(update: Update, context: CallbackContext) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    print(answer)
    poll_id = answer.poll_id
    try:
        questions = context.bot_data[poll_id]["questions"]
    # this means this poll answer update is from an old poll, we can't do our answering then
    except KeyError:
        return
    selected_options = answer.option_ids
    answer_string = ""
    global all_data
    global total_num_ans
    if answer['user']['id'] not in all_data:
        all_data[answer['user']['id']] = 0 
    if questions[selected_options[0]] == "Yes":
        all_data[answer['user']['id']] = all_data.get(answer['user']['id'],0) + 1
    total_num_ans[answer['user']['id']] = total_num_ans.get(answer['user']['id'],0) + 1
    if total_num_ans[answer['user']['id']] == 10 and all_data[answer['user']['id']]/10.0 > 0.5:
        context.bot.send_message(
            context.bot_data[poll_id]["chat_id"],
            f"user ID {answer['user']['id']} yes counts {all_data[answer['user']['id']]}", # prints dictionary that collects reponse in all_data
            parse_mode=ParseMode.HTML,)
    elif total_num_ans[answer['user']['id']] == 10:
        context.bot.send_message(context.bot_data[poll_id]["chat_id"],
            f"{update.effective_user.mention_html()}, you are fine :)", # prints dictionary that collects reponse in all_data
            parse_mode=ParseMode.HTML,)


def help_handler(update: Update, _: CallbackContext) -> None:
    """Display a help message"""
    update.message.reply_text("Learn more at https://amyphenjati.github.io/team_asia/learn_more.html")


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('poll', poll))
    dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))  
    dispatcher.add_handler(CommandHandler('help', help_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()