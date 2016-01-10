#! /usr/bin/python

import my_secret as ms

from telegram import Updater
updater = Updater(token=ms.token)
dispatcher = updater.dispatcher

def echo(bot, update):
	print(update)
	
def deleteme(bot,update):
	print("delete")

def addme(bot,update):
	print("add")

def notunderstand(bot,update):
	bot.sendMessage(chat_id=update.message.chat_id, text="/add : dich anmelden\n/delete : dich abmelden")
	
dispatcher.addTelegramCommandHandler('delete', deleteme)
dispatcher.addTelegramCommandHandler('add', addme)
dispatcher.addTelegramMessageHandler(echo)
dispatcher.addUnknownTelegramCommandHandler(notunderstand)

updater.start_polling(5)
