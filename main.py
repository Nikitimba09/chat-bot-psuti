import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Популярные ароматы")
    item2 = types.KeyboardButton("Советы по выбору")
    item3 = types.KeyboardButton("Информация о парфюме")
    item4 = types.KeyboardButton("Контакты")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Добро пожаловать в парфюмерный бот! Выберите опцию:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Популярные ароматы":
        bot.send_message(message.chat.id,
                         "Вот несколько популярных ароматов:\n1. Chanel No. 5\n2. Dior Sauvage\n3. Gucci Bloom "
                         "\n4. САНЁК")
    elif message.text == "Советы по выбору":
        bot.send_message(message.chat.id,
                         "Вот несколько советов по выбору аромата:\n- Учитывайте время года.\n- Пробуйте аромат на "
                         "коже.\n- Не спешите с выбором.")
    elif message.text == "Информация о парфюме":
        bot.send_message(message.chat.id,
                         "Парфюм состоит из верхних, средних и базовых нот. Каждая нота раскрывается в разное время.")
    elif message.text == "Контакты":
        bot.send_message(message.chat.id, "Вы можете связаться с нами по электронной почте: contact@parfume-bot.com")


if __name__ == '__main__':
    bot.polling(none_stop=True)
