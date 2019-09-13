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

def star(bot,update):
    k=update.message.text
    if k=='Mars':
        mars = ephem.Mars(time.time())
        const=ephem.constellation(mars)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Mercury':
        mercury = ephem.Mercury(time.time())
        const=ephem.constellation(mercury)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Venus':
        venus = ephem.Venus(time.time())
        const=ephem.constellation(venus)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Earth':
        earth = ephem.Earth(time.time())
        const=ephem.constellation(earth)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Jupiter':
        jupiter = ephem.Jupiter(time.time())
        const=ephem.constellation(jupiter)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Saturn':
        saturn = ephem.Saturn(time.time())
        const=ephem.constellation(saturn)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Uranus':
        uranus = ephem.Uranus(time.time())
        const=ephem.constellation(uranus)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Neptune':
        neptune = ephem.Neptune(time.time())
        const=ephem.constellation(neptune)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    elif k=='Pluto':
        pluto = ephem.Pluto(time.time())
        const=ephem.constellation(Pluto)
        update.message.reply_text(f'Сегодня планета {k} находится в созвездии {const}')
    else: 
        text="Такой планеты не существует"
        update.message.reply_text(text)

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

