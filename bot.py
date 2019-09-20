from glob import glob
import logging
from random import choice
import ephem
import time


from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

import settings


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot,update,user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text='Привет {}'.format(emo)
    update.message.reply_text(text, reply_markup = get_keyboard)
#
#def planet(bot,update,user_data):
#  m='Введите название планеты (например: "Mars"): '
#  update.message.reply_text(m)
#
#space = {'Mars': ephem.Mars(time.time()), 'Mercury': ephem.Mercury(time.time()), 
#            'Venus': ephem.Venus(time.time()), 'Jupiter': ephem.Jupiter(time.time()), 
#            'Saturn': ephem.Saturn(time.time()), 'Uranus': ephem.Uranus(time.time()), 
#            'Neptune': ephem.Neptune(time.time()), 'Pluto': ephem.Pluto(time.time()) }
#
#def star(bot,update,user_data):
#    planet=update.message.text
#    if planet in space:
#        my_planet=space[planet]
#        const=ephem.constellation(my_planet)
#        update.message.reply_text(f'Сегодня планета {planet} находится в созвездии {const}')
#    else:   
#        update.message.reply_text('такой планеты не существует')

def talk_to_me(bot,update,user_data):
        emo = get_user_emo(user_data)
        user_text = "Привет,{} {}! Ты написал: {}".format(update.message.chat.first_name, emo,
                 update.message.text)
        logging.info("User: %s, Chat id: %s, Message: %s",update.message.chat.username,
                update.message.chat.id,update.message.text)
        update.message.reply_text(user_text,reply_markup = get_keyboard())

def send_cat_picture(bot, update,user_data):
    cat_list = glob('images/cat*jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id = update.message.chat.id, photo=open(cat_pic,'rb'), reply_markup = get_keyboard())

def change_avatar(bot,update,user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Готово: {}'.format(emo),reply_markup = get_keyboard())

def get_contact(bot,update,user_data):
    print(update.message.contact)
    update.message.reply_text('Спасибо, {}.'.format(update.message.chat.first_name),reply_markup = get_keyboard())


def get_location(bot,update,user_data):
    print(update.message.location)
    update.message.reply_text('Спасибо, {}.'.format(get_user_emo(user_data)),reply_markup = get_keyboard())

def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']


def get_keyboard():
    contact_button = KeyboardButton('Прислать контакты', request_contact=True) 
    location_button = KeyboardButton('Прислать координаты', request_location=True) 
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Прислать котика', 'Сменить аватарку'],
                                        [contact_button,location_button]
                                       ], resize_keyboard=True
                                      )
    return my_keyboard
def main():
    mybot = Updater(settings.API_KEY,request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user, pass_user_data=True))
    #dp.add_handler(CommandHandler('planet',planet, pass_user_data=True))
    dp.add_handler(CommandHandler('cat',send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Прислать котика)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сменить аватарку)$', change_avatar, pass_user_data=True))
    #dp.add_handler(MessageHandler(Filters.text, star, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()

main()

