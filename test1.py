#! /usr/bin/python

import my_secret as ms

from telegram import Updater
updater = Updater(token=ms.token)
dispatcher = updater.dispatcher

def echo(bot, update):
	bot.sendMessage(chat_id=ms.usr_id, text=update.message.chat.first_name+": "+update.message.text)	
	print(update)
	
dispatcher.addTelegramMessageHandler(echo)

updater.start_polling()
