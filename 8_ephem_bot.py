"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import settings
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')


def greet_user(update, context):
	text = 'Вызван /start'
	print(text)
	update.message.reply_text(text)


def talk_to_me(update, context):
	user_text = update.message.text
	print(user_text)
	update.message.reply_text(user_text)


def constell(update, context):

	input_text = update.message.text.split()
	planet = input_text[1]
	date = input_text[2]
	if planet == 'Mars':
		mars = ephem.Mars(date)
		constellation = ephem.constellation(mars)[1]

	elif planet == 'Mercury':
		mercury = ephem.Mercury(date)
		constellation = ephem.constellation(mercury)[1]

	elif planet == 'Saturn':
		saturn = ephem.Saturn(date)
		constellation = ephem.constellation(saturn)[1]
	print(f'{planet} in {constellation}')
	update.message.reply_text(constellation)


def main():
	mybot = Updater(settings.API_KEY, use_context=True)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(CommandHandler('planet', constell))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	logging.info("Бот стартовал.")
	mybot.start_polling()
	mybot.idle()


if __name__ == "__main__":
	main()
