import telebot
bot = telebot.TeleBot('907189205:AAHfVFSyUVI37R60jq3F2kheyF_zBkZZbOc')

name = '' 

@bot.message_handler(content_types=['text', 'document', 'audio'])

def start(message):
	if message.text == '/start':
		bot.send_message(message.from_user.id, "Привіт, я - вірний помічник команди Franchise Group!") 
		bot.send_message(message.from_user.id, "Як я можу до вас звертатись?")
		bot.register_next_step_handler(message, get_name)

	

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Дуже приємно, '+str(name)+'!') 
    bot.send_message(message.from_user.id, 'Тримайте свій подарунок! Виступ Мирослави Козачук на BlackFest з темою: "Франчайзинг як ефективний метод управління закладами" \n\n https://youtu.be/kr8Xz3rorBk')

	



bot.polling(none_stop=True, interval=0)