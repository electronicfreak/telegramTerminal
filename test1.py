#! /usr/bin/python

import my_secret as ms

from telegram import Updater
updater = Updater(token=ms.token)
dispatcher = updater.dispatcher

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
	print(update.message.text)
	
dispatcher.addTelegramMessageHandler(echo)

updater.start_polling()
