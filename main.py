import telebot

# Твой токен и chat_id (вставлены прямо в код)
TELEGRAM_TOKEN = "8337596694:AAGdBueLe8EUnu3zhvM6wO_oHhxCcvnHMt0"
CHAT_ID = "663371928"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот успешно запущен на Render!")

# Простой запуск (long polling)
if __name__ == "__main__":
    bot.infinity_polling()
