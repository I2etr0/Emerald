import telebot
from telebot import types
import var
from var import token
import logging
import get_ip
import time

token = var.token
bot = telebot.TeleBot(f'{token}')

#TODO: Настроить логирование (EMERALD-6)



@bot.message_handler(commands=['start'])
def handle_start(message):
  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('Получить IP')
  button2 = types.KeyboardButton('Soon')
  keyboard.add(button1, button2)

  # Запись пинкода в переменную
  #TODO: Настроить безопасность данных бота (EMERALD-7)
  bot.send_message(message.chat.id, 'Доброго времени суток! Я Эмеральд!')
  time.sleep(0.7)
  bot.send_message(message.chat.id, 'Пожалуйста, введите Ваш PIN-код')
  def echo_message(message):
    messages = []
    text = message.text
    messages.append(text)

    print(messages)

@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
  
  # Ответ на текстовое сообщение
  if message.text == 'Получить IP':
      bot.send_message(message.chat.id, f'Ваш ip адрес: {get_ip.ip}')
  
  # Ответ на изображение
  if message.photo:
      bot.send_message(message.chat.id, 'Вы отправили изображение.')
  
  # Ответ на стикер
  if message.sticker:
      bot.send_message(message.chat.id, 'Вы отправили стикер.')

bot.polling()