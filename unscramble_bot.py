import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# unscramble
from unscramble import Unscramble
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! write something like "lustrfe" and I am going to unscramble that!')


def echo(update: Update, _: CallbackContext) -> None:
    u = Unscramble()
    text_recived = update.message.text
    permuted_text = u.permute_text(text=text_recived)
    valid_word = u.search_valid_us_word(arr=permuted_text)
    if len(valid_word) >= 1:

        for w in valid_word:
            """Echo the user message."""
            update.message.reply_text(f'The word could be: {w}!')
    else:
        update.message.reply_text('Hey! there are not a word in this world')


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.environ.get('TOKEN_BOT'))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


