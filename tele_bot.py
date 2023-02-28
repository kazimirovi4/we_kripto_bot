from key import TOKEN, SECRET, APIKEY
import telebot
import ccxt

token = TOKEN
bot = telebot.TeleBot(token)


api_key = APIKEY
secret = SECRET


we = ccxt.wavesexchange()
market_we = we.load_markets()
BTC_USDT = list(market_we.items())[69:70]
last_price = str(we.fetch_ticker('BTC/USDT')['last']) + " 'USDT'"

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    price = telebot.types.InlineKeyboardButton(text='Узнать курс', callback_data='price')
    btc_usdt = telebot.types.InlineKeyboardButton(text='Обменять BTC на USDT',
                                                  url='https://waves.exchange/trading/spot/BTC_USDT')
    usdt_btc = telebot.types.InlineKeyboardButton(text='Обменять USDT на BTC',
                                                  url='https://waves.exchange/trading/spot/BTC_USDT')
    keyboard.add(price, btc_usdt, usdt_btc)
    bot.send_message(message.chat.id, 'Нажмите на кнопку для обмена валюты', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_course(callback):
    if callback.data == 'price':
        bot.send_message(callback.message.chat.id, last_price)


bot.infinity_polling()