import telebot
from telebot import types
from config import token
from config import regions
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rmk.add(types.KeyboardButton('auther'), types.KeyboardButton('Найти регион'))

    msg = bot.send_message(message.chat.id, '<b>Выберите нужный блок!</b>', parse_mode='html', reply_markup=rmk)
    bot.register_next_step_handler(msg, menu)

def menu(message):
    if message.text == 'Найти регион':
        rkm = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rkm.add(types.KeyboardButton('Назад'))
        msg = bot.send_message(message.chat.id, '<b>Напишите какой регион вас интересует!</b>', parse_mode='html', reply_markup=rkm)
        bot.register_next_step_handler(msg, get_regions)

    elif message.text == 'auther':
        rkm = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rkm.add(types.KeyboardButton('Назад'))
        msg = bot.send_message(message.chat.id, '<b>Не твоё дело...)</b>', parse_mode='html', reply_markup=rkm)
        bot.register_next_step_handler(msg, start)

    else:
        rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rmk.add(types.KeyboardButton('auther'), types.KeyboardButton('Найти регион'))

        msg = bot.send_message(message.chat.id, '<b>Выберите нужный блок!</b>', parse_mode='html', reply_markup=rmk)
        bot.register_next_step_handler(msg, menu)

def get_regions(message):

    if message.text in regions:
        rkm = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rkm.add(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, f'<b>{regions.get(message.text)}</b>', parse_mode='html')
        msg = bot.send_message(message.chat.id, '<b>Напишите какой регион вас интересует!</b>', parse_mode='html', reply_markup=rkm)
        bot.register_next_step_handler(msg, get_regions)

    elif message.text == 'Найти регион':
        msg = bot.send_message(message.chat.id, '<b>Напишите какой регион вас интересует!</b>', parse_mode='html')
        bot.register_next_step_handler(msg, get_regions)

    elif message.text == 'Назад':
        rkm = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rkm.add(types.KeyboardButton('auther'), types.KeyboardButton('Найти регион'))
        msg = bot.send_message(message.chat.id, '<b>Выберите нужный блок!</b>', parse_mode='html', reply_markup=rkm)
        bot.register_next_step_handler(msg, menu)

    else:
        rkm = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rkm.add(types.KeyboardButton('Назад'))
        bot.send_message(message.chat.id, f'<b>Регион: {message.text} нету у нас в базе!</b>', parse_mode='html')
        msg = bot.send_message(message.chat.id, '<b>Напишите другой регион!</b>', parse_mode='html', reply_markup=rkm)
        bot.register_next_step_handler(msg, get_regions)


bot.polling(none_stop=True)