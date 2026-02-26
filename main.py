import telebot
from config import TOKEN
from ai_handler import ask_ai

bot = telebot.TeleBot(TOKEN)
help_text = """
/start - приветствие
/help - список команд
/помощь - спроси у эксперта по экологии что тебе делать!
"""


@bot.message_handler(commands = ['start'])
def send_start(message):
    bot.reply_to(message, "Привет! Я твой гид в загадочном мире экологии! Напиши /help, дабы увидеть больше команд")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['помощь'])
def ai_command(message):
    user_text = message.text.replace('/помощь', '', 1).strip()
    if not user_text:
        bot.reply_to(message, "Напиши текст после команды.\n\nПример:\n/помощь Привет, как дела?")
        return
    user_text = user_text[:1000]
    try:
        bot.send_chat_action(message.chat.id, "typing")
        reply = ask_ai(user_text)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "⚠ Ошибка при обращении к эксперту.")
        print(e)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.delete_webhook()
bot.polling()
