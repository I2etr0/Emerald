import telebot
# from telebot import types
import var
from var import token
import logging

import get_ip

token = var.token

bot = telebot.TeleBot(f'{token}')

@bot.message_handler(commands=['start'])
def handle_start(message):
  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('Получить IP')
  button2 = types.KeyboardButton('Soon')
  keyboard.add(button1, button2)

  # Отправка сообщения с клавиатурой
  bot.reply_to(message, 'Привет! Я бот.', reply_markup=keyboard)

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