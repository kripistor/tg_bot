import logging
import telebot
import random
import requests
from config import bot
from telebot import types
import geocoder
import time
f = open('logs.txt')
logger = telebot.logger
zz = ['Овен','Телец','Близнецы','Лев','Дева','Весы','Скорпион','Стрелец','Козерог', 'Водолей','Рыбы']
rr = ['Ты гей', 'ты лох', 'Ты напишшеь егэ на 0 баллов']

photo_list = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Салам, {message.from_user.first_name}' , parse_mode='html')
    bot.send_message(message.chat.id, 'Вот список досутпных команд: '+ '\n' + 'Как меня зовут?'+ '\n'+ 'Привет'+ '\n' + 'Гороскоп' + '\n'+'Скинь фото' '\n' + 'Рандомный факт')
@bot.message_handler(content_types='text')
def get_user_text(message):
    if message.text == 'Как меня зовут?':
        bot.send_message(message.chat.id,'Ты че, долбоеб? Не знаешь как тебя зовут?', parse_mode='html')
        time.sleep(1)
        bot.send_message(message.chat.id, f'Ну ладно, тебя зовут: {message.from_user.first_name} ', parse_mode='html')
    elif message.text == 'Привет':
        bot.send_message(message.chat.id,'Здоровее видали')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Ну и пошел нахуй)')
    elif message.text == 'Гороскоп':
        msg = bot.send_message(message.from_user.id, 'Скажи свой зз')
        bot.register_next_step_handler(msg,zodiac_signs)
    elif message.text == 'Скинь фото':
        photo = open('1.png','rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Рандомный факт':
        f = random.choice(rr)
        bot.send_message(message.chat.id, 'Рандомный факт: ' + f)
    else:
        bot.send_message(message.chat.id, 'Моя твоя не понимать')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Ну и пошел нахуй)')

def zodiac_signs(message):
    z = message.text
    if z in zz:
        bot.send_message(message.chat.id,f'{z}, ахахах, ну ты и лох, завтра сдохнешь, клоун')
    elif z == 'Рак':
        bot.send_message(message.chat.id,'ахахах, какое совпадение')
    else:
        bot.send_message(message.chat.id, 'Ты конченный ? Это не зз, напиши нормально')
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)
