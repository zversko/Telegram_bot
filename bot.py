import telebot
import config
import calcul
import class_directory.m_search
import re
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    '''
    Приветствие с иконкой и с информацией о функциях
    '''
    sti = open('picture/wellcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Калькулятор")
    item2 = types.KeyboardButton("Справочник")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def menu_homework(message):
    '''
    Выбор из меню
    '''
    # if message.chat.type == 'group':
    if message.text == 'Калькулятор':
        bot.send_message(message.chat.id, 'Вводить в таком формате 4 + (-1)^0.5 - 1 + 8 * (-1)^0.5 - 4 / (-1)^0.5')
        bot.send_message(message.chat.id, '(-1)^0.5 - Квадратный корень из (-1)')
        bot.register_next_step_handler(message, calc)
    elif message.text == 'Справочник':
        bot.send_message(message.chat.id, 'Укажите данные для поиска (например, "иван егор")')
        bot.register_next_step_handler(message, directory)
    else:
        bot.send_message(message.chat.id, 'Такого выбора нет в моем меню')

def calc(message):
    '''
    Вызов функции калькулятора, с проверкой на недопустимые символы
    '''
    # if message.chat.type == 'group':
    if re.match(r'''[a-z|A-Z|\+|\/|\*|\^]+''', message.text):
        bot.send_message(message.chat.id, 'Недопустимые символы ')
    else:
        bot.send_message(message.chat.id, str(calcul.calculator(message.text)))
        # send_message(message.chat.id, calculate.calculator(message.text))

def directory(message):
    '''
    Вызов функции поисковика по справочнику
    '''
    bot.send_message(message.chat.id, str(class_directory.m_search.contact_finder(message.text)))
 
# RUN
bot.polling(none_stop=True)