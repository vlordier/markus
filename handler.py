from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler, MessageHandler, Filters
import random
import requests
from bs4 import BeautifulSoup
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import emoji
from langdetect import detect


here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))


TOKEN = "some_token_given_by_Telegram_Bot_Father" #MarcusAurelius_Bot
TOKEN = os.environ['TELEGRAM_TOKEN']


questions = ["How do I feel ?", "How am I better ? How can I improve ?", "What did I do wrong ? What did I do right ?", "What did I do which was unfriendly, unsocial, or uncaring ?", "What duty is left undone ?", \
"Today was a good day because ...", "What did I do to make my future better ?", "What is important to me ?"]

i = 0
max_quote_pages = 10


def moji(text):
    return emoji.emojize(text, use_aliases=True)

def get_quote():
    p = random.randint(1, max_quote_pages)
    url="https://www.goodreads.com/quotes/tag/stoicism?page="+str(p)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_quotes = soup.findAll("div", {"class": "quoteText"})
    q = random.randint(0, len(all_quotes))
    quote_of_the_day = all_quotes[q].getText().split("//<![CDATA[",1)[0].rstrip().strip().replace('\r', '').replace('\n', '')
    while detect(quote_of_the_day) != 'en':
        print(detect(quote_of_the_day))
        q = random.randint(0, len(all_quotes))
        quote_of_the_day = all_quotes[q].getText().split("//<![CDATA[",1)[0].rstrip().strip().replace('\r', '').replace('\n', '')
    return quote_of_the_day

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Stoic bot. Review your day with me")
    bot.send_message(chat_id=update.message.chat_id, text=get_quote())
    button_list = [[moji(':grinning:'), moji(':neutral_face:'), moji(':worried:')], [moji(':scream:'),moji('🤩'),moji('🤷🏻‍♂️')]]#, 'top-right'], ['bottom-left', 'bottom-right']]
#   button_list = [[KeyboardButton(s)] for s in some_strings]
    reply_markup = ReplyKeyboardMarkup(button_list)


    bot.send_message(chat_id=update.message.chat_id, text=questions[0], reply_markup=reply_markup)

    global i
    i=0
    i+=1

def review_day(bot, update):
    global i

#    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    if i < len(questions):
        bot.send_message(chat_id=update.message.chat_id, text=questions[i], reply_markup=ReplyKeyboardRemove())
        i+=1
    else :
        some_strings = ["/start"]
        button_list = [[KeyboardButton(s)] for s in some_strings]
        reply_markup = ReplyKeyboardMarkup(button_list)

        bot.send_message(chat_id=update.message.chat_id, text="Report completed.")
        bot.send_message(chat_id=update.message.chat_id, text="Well done.\n\n Keep going ;)", reply_markup=reply_markup)
        i=0


def main():

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    updater = Updater(token=TOKEN)
    job_queue = updater.job_queue


    start_handler   = CommandHandler('start', start)
    day_handler = MessageHandler(Filters.text, review_day)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(day_handler)


    updater.start_polling()
    updater.idle()




if __name__ == '__main__':
    main()