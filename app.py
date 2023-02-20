import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

# import callback functions
from bot import (
    start,
    inline_hanlerlar,
    back_handler
)

app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return {'status': 200}

    elif request.method == 'POST':
        # get data from request
        data: dict = request.get_json(force=True)

        # convert data to Update obj
        update: Update = Update.de_json(data, bot)

        # Dispatcher
        dp: Dispatcher = Dispatcher(bot, None, workers=0)

        # handlers
        dp.add_handler(CommandHandler('start',start))
        # Add handler for photo message
        dp.add_handler(CallbackQueryHandler(inline_hanlerlar,pattern='shahar'))
        dp.add_handler(CallbackQueryHandler(back_handler,start))

        # process update
        dp.process_update(update=update)

        return {'status': 200}

bot = Bot(token=TOKEN)
print(bot.get_webhook_info())