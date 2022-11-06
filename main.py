import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started")

def start_command(update, context):
    update.message.reply_text('Il bot è stato avviato correttamente')

def help_command(update, context):
    update.message.reply_text("Se ti serve qualcosa, cerca su Google")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher
     
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()