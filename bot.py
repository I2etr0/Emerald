import telebot
from telebot import types
import file
from file import stoken 
import termcolor
from termcolor import colored

token = file.stoken

bot = telebot.TeleBot(f'{token}')

@bot.message_handler(commands=['start'])
def handle_start(message):
  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(row_width=1)
  #button1 = types.KeyboardButton('Получить IP')
  button2 = types.KeyboardButton('Soon')
  keyboard.add(button2)

  # Отправка сообщения с клавиатурой
  bot.reply_to(message, 'Привет! Меня зовут Эмеральд. Чем я могу тебе помочь?', reply_markup=keyboard)

@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
  
  # Ответ на текстовое сообщение
  if message.text == 'Soon':
      bot.send_message(message.chat.id, f'{message.text} это секретная разработка!\nО ней пока никто не знает! Даже разработчики!')
   
  # Ответ на изображение
  if message.photo:
      bot.send_message(message.chat.id, 'Вы отправили изображение.')
  
  # Ответ на стикер
  if message.sticker:
      bot.send_message(message.chat.id, 'Вы отправили стикер.')

bot.polling()