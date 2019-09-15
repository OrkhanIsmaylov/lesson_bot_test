from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import time


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot,update):
    text='Выполнена команда /start'
    logging.info(text)
    update.message.reply_text(text)

def planet(bot,update):
   m='Введите название планеты (например: "Mars"): '
   update.message.reply_text(m)

space = {'Mars': ephem.Mars(time.time()), 'Mercury': ephem.Mercury(time.time()), 
            'Venus': ephem.Venus(time.time()), 'Jupiter': ephem.Jupiter(time.time()), 
            'Saturn': ephem.Saturn(time.time()), 'Uranus': ephem.Uranus(time.time()), 
            'Neptune': ephem.Neptune(time.time()), 'Pluto': ephem.Pluto(time.time()) }

def star(bot,update):
    planet=update.message.text
    if planet in space:
        my_planet=space[planet]
        const=ephem.constellation(my_planet)
        update.message.reply_text(f'Сегодня планета {planet} находится в созвездии {const}')
    else: 
        update.message.reply_text('такой планеты не существует')
    

#def talk_to_me(bot,update):
#    user_text = "Привет,{}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
#    logging.info("User: %s, Chst id: %s, Message: %s",update.message.chat.username,
#                update.message.chat.id,update.message.chat.text)
#    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY,request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet',planet))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, star))

    mybot.start_polling()
    mybot.idle()

main()

