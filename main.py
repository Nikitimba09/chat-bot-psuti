import telebot
from telebot import types
from dotenv import load_dotenv
import os
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.info(f"Пользователь {message.chat.id} отправил команду /start")

    web_app_url = "https://nikitimba09.github.io/chat-bot-psuti/"  # URL вашего Web App
    keyboard = types.InlineKeyboardMarkup()
    web_app_button = types.InlineKeyboardButton(text="Открыть Web App", web_app=types.WebAppInfo(web_app_url))
    keyboard.add(web_app_button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы открыть Web App", reply_markup=keyboard)

# Обработчик данных от веб-приложения
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(web_app_message):
    item = web_app_message.web_app_data.data  # Получаем данные
    logging.info(f"Получены данные из веб-приложения: {item} от пользователя {web_app_message.chat.id}")

    if item == "popular":
        bot.send_message(web_app_message.chat.id, "Вот несколько популярных ароматов:\n1. Chanel No. 5\n2. Dior Sauvage\n3. Gucci Bloom")
    elif item == "advice":
        bot.send_message(web_app_message.chat.id, "Вот несколько советов по выбору аромата:\n- Учитывайте время года.\n- Пробуйте аромат на коже.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    logging.info(f"Получено сообщение: {message.text} от пользователя {message.chat.id}")

    if message.text == "Популярные ароматы":
        bot.send_message(message.chat.id,
                         "Вот несколько популярных ароматов:\n1. Chanel No. 5\n2. Dior Sauvage\n3. Gucci Bloom")
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
    logging.info("Бот запущен и готов к работе")
    bot.polling(none_stop=True)
