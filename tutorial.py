import telebot
from telebot import types
from var import token

bot = telebot.TeleBot(f'{token}')

@bot.message_handler(commands=['start'])
def handle_start(message):

  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('Кнопка 1')
  button2 = types.KeyboardButton('Кнопка 2')
  button3 = types.KeyboardButton('Кнопка 3')
  keyboard.add(button1, button2, button3)

  # Отправка сообщения с клавиатурой
  bot.reply_to(message, 'Привет! Я бот.', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):

  if message.text == 'Кнопка 1':
      # Действия при нажатии на кнопку 1
      bot.reply_to(message, 'Вы нажали на Кнопку 1')

  elif message.text == 'Кнопка 2':
      # Действия при нажатии на кнопку 2
      bot.reply_to(message, 'Вы нажали на Кнопку 2')

  elif message.text == 'Кнопка 3':
      # Действия при нажатии на кнопку 3
      bot.reply_to(message, 'Вы нажали на Кнопку 3')
  else:
      # Действия при получении другого сообщения
      bot.reply_to(message, 'Получено сообщение: ' + message.text)


@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
  
  # Ответ на текстовое сообщение
  if message.text == 'Привет':
      bot.send_message(message.chat.id, 'Привет! Как дела?')
  
  # Ответ на изображение
  if message.photo:
      bot.send_message(message.chat.id, 'Вы отправили изображение.')
  
  # Ответ на стикер
  if message.sticker:
      bot.send_message(message.chat.id, 'Вы отправили стикер.')

bot.polling()