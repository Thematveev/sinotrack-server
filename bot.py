from telebot import TeleBot
from database import Cords


bot = TeleBot('5806041163:AAG3F_eOFBztryotOQG5C9_KO0Y7t7otsN8')

@bot.message_handler(commands=['position'])
def position_handler(message):
    data = Cords.select().order_by(Cords.time.desc()).get()
    bot.send_message(message.chat.id, f"http://maps.google.com/maps?q=+{data.lat},+{data.lon}")
    bot.send_message(message.chat.id, data.time)


bot.polling()