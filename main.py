from email import message
import telebot
from telebot import types

bot = telebot.TeleBot('5699728400:AAEh0Bj3WsJiFA_xzBsgyczlqrzaIlG-HN0')


@bot.message_handler(commands=['start'])
def start(message):
    messname = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, messname , parse_mode='html')

'''
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет!" , parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('Image.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю!" , parse_mode='html')
'''

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, f"Лайк!")

@bot.message_handler(commands=['help'])
def ButtonCommands(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    startButton = types.KeyboardButton('Начать')
    exitButton = types.KeyboardButton('Остановить')
    markup.add(startButton, exitButton)
    bot.send_message(message.chat.id, 'Работает!!!' , reply_markup=markup)

@bot.message_handler(commands=['website'])
def website(message):
    markupweb = types.InlineKeyboardMarkup()
    markupweb.add(types.InlineKeyboardButton("Перейти на вебсайт", url="https://www.youtube.com/"))
    bot.send_message(message.chat.id, 'Перейти на сайт' , reply_markup=markupweb)



bot.polling(none_stop=True)