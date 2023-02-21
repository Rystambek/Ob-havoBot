from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from db import DB
import os
import requests
db = DB('Ob-havoBot/db.json')
Token = os.environ['TOKEN']

def ob_havo(city):
    basic_url = db.city(city)
    response = requests.get(basic_url)
    data = response.json()

    temp = data['main']
    temp_min = round(temp['temp_min']-281)
    temp_max = round(temp['temp_max']-273)
    return temp_min, temp_max


def start(update:Update, context:CallbackContext):
    bot = context.bot
    user = update.message.from_user.first_name
    chat_id = update.message.chat.id
    text = f"Assalomu alaykum {user}\nBu yerdan Shahar yoki Viloyat tanlang"
    keyboard = InlineKeyboardMarkup(city())
    bot.sendMessage(chat_id=chat_id,text=text,reply_markup=keyboard)

def city():
    return [
        [InlineKeyboardButton('Toshkent',callback_data='shahar Toshkent'),
         InlineKeyboardButton('Samarqand',callback_data='shahar Samarqand')],
        [InlineKeyboardButton('Navoiy',callback_data='shahar Navoiy'),
         InlineKeyboardButton('Buxoro',callback_data='shahar Buxoro')],
        [InlineKeyboardButton('Xorazm',callback_data='shahar Xorazm'),
         InlineKeyboardButton('Jizzax',callback_data='shahar Jizzax')],
         [InlineKeyboardButton('Surqandaryo',callback_data='shahar Surqandaryo'),
         InlineKeyboardButton('Qashqadaryo',callback_data='shahar Qashqadaryo')],
        [InlineKeyboardButton("Farg'ona",callback_data="shahar Farg'ona"),
         InlineKeyboardButton('Namangan',callback_data='shahar Namangan')],
         [InlineKeyboardButton("Andijon",callback_data="shahar Andijon"),
         InlineKeyboardButton('Sirdaryo',callback_data='shahar Sirdaryo')],
         [InlineKeyboardButton('Qoraqalpoq',callback_data='shahar Qoraqalpoq')]
    ]

def back():
    return [
        [InlineKeyboardButton('Orqaga', callback_data='back01')]
    ]

def inline_hanlerlar(update:Update,context:CallbackContext):
    bot = context.bot
    query = update.callback_query
    chat_id = query.message.chat_id
    data,city = query.data.split()

    min,max = ob_havo(city)

    bot.sendMessage(chat_id=chat_id,text = f"Bugun {city}da havo o'zgarib turadi \nMin +{min}°\nMax +{max}° \n bo'lishi kutilmoqda",
                                reply_markup = InlineKeyboardMarkup(back()))
    
def back_handler(update:Update,context:CallbackContext):
    bot = context.bot
    query = update.callback_query
    chat_id = query.message.chat_id
    data = query.data

    if data == "back01":
            bot.sendMessage(
                chat_id = chat_id,
                text=f"Bu yerdan Shahar yoki Viloyat tanla",
                reply_markup = InlineKeyboardMarkup(city())
            )

def main():
    
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler('start',start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_hanlerlar,pattern='shahar'))
    updater.dispatcher.add_handler(CallbackQueryHandler(back_handler,start))
    updater.start_polling()
    updater.idle()


# if __name__ == "__main__":
#     main()