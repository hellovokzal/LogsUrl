from requests import *
from os import *
from telebot import *

bot = TeleBot("6518733446:AAHUw0uM9hzLWBrsY9hZ1_B20SYcB-bu-jg")

text =  ""
text1 = ""
type_url = input("Введите ссылку:  ")

while True:
	url = get(type_url)
	if text == url.text:
		text1 = ""
	else:
		bot.send_message(1477069902,  f"{url.text}")
		text = url.text
bot.polling(none_stop=True)
