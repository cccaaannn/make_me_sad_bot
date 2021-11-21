from telegram.ext import Updater, CommandHandler
import logging
import sys
import os

from currency_api import currency_api 

class telegram_bot:
    def __init__(self) -> None:
        api_key_env_path = "TELEGRAM_BOT_KEY"
        logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", handlers=[logging.StreamHandler()])
        try:
            self.api_key = os.environ[api_key_env_path]
            self.c_api = currency_api()
        except:
            logging.error("Could not get the api key from {0}".format(api_key_env_path), exc_info=True)
            sys.exit()

    def run_bot(self):
        def error(update, context):
            logging.error('Update "%s" caused error "%s"', update, context.error)


        def help(update, context):
            update.message.reply_text("/dollar to make yourself sad\n/dollar 10 to make yourself even sadder")
            logging.info("help used username:{0}".format(update.message.from_user.username))

        def get_dollar(update, context):
            try:
                if(len(context.args) > 0):
                    arg0 = context.args[0]
                    tl = self.c_api.request_to_api()
                    response = float(tl) * float(arg0)
                    update.message.reply_text(response)
                else:
                    response = self.c_api.request_to_api()
                    logging.info(response)
                    update.message.reply_text(response)
            except Exception as e:
                logging.error("username:{0}".format(update.message.from_user.username), exc_info=True)
                update.message.reply_text("incorrect parameters passed")

        # bot loop
        logging.info("Bot starting")
        updater = Updater(self.api_key, use_context=True)

        # command handler
        updater.dispatcher.add_handler(CommandHandler("dollar", get_dollar, pass_args=True))
        updater.dispatcher.add_handler(CommandHandler("help", help))

        # error handler
        updater.dispatcher.add_error_handler(error)

        updater.start_polling()
        updater.idle()

