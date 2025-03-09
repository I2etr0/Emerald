import telebot
from telebot import types
import file
from file import stoken 
import re


token = file.stoken
bot = telebot.TeleBot(f'{token}')

#TODO: Настроить логирование (EMERALD-6)



@bot.message_handler(commands=['start'])
def handle_start(message):
  # Создание кнопок первого уровня
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
  button1 = types.KeyboardButton('Получить ID')
  button2 = types.KeyboardButton('Перейти к ИИ')
  keyboard.row(button1, button2)


  # Отправка сообщения с клавиатурой
  bot.reply_to(message, 'Привет! Меня зовут Эмеральд. Чем я могу тебе помочь?', reply_markup=keyboard)


@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
  # Добавление кнопок второго уровня. Они будут под сообщением
  if message.text == 'Перейти к ИИ':
    keyboard = types.InlineKeyboardMarkup(row_width=1) # Обрати внимение, что тут тип кнопки InlineKeyboardMarkup, а в первой итерации кнопок ReplyKeyboardMarkup и KeyboardButton!
    button1 = types.InlineKeyboardButton('Qwen', url='https://chat.qwen.ai/')
    button2 = types.InlineKeyboardButton('DeepSeek', url='https://chat.deepseek.com/')
    keyboard.row(button1, button2)
    bot.send_message(message.chat.id, f'Какой бот Вам интересен?', reply_markup=keyboard)


  elif message.text == 'Получить ID':
    bot.send_message(message.chat.id, f'<b>{message.from_user.id}</b> - это Ваш ID, но учтите, что его надо держать в секрете!!!', parse_mode='HTML')
  
  elif message.text == 'Ты тут?' or message.text == 'Ты здесь?':
    bot.send_message(message.chat.id, 'Да, Милорд, я здесь. Чем могу помочь?')

  elif message.text == 'ping' or message.text == 'Ping':
    bot.send_message(message.chat.id, 'Да-да?')

  elif message.text == 'Как дела?' or message.text == 'как дела?':
    bot.send_message(message.chat.id, 'Если я Вам могу ответить, значит, сервера работают и у меня все хорошо! \n\nЧем я могу Вам помочь?')

  elif message.text == 'Привет!' or message.text == 'привет' or message.text == 'привет!' or message.text == 'Привет' or message.text == 'ghbdtn' or message.text == 'ghbdtn!'  or message.text == 'Ghbdtn!' or message.text == 'Ghbdtn':
    bot.send_message(message.chat.id, 'Доброго времени суток, Милорд. Чем могу помочь?')

  else:
    bot.send_message(message.chat.id, 'Я не очень Вас понимаю, но обязательно передам Ваше сообщение разработчикам!')

        
    
  # Ответ на изображение
  if message.photo:
      bot.send_message(message.chat.id, 'Вы отправили изображение.')

  # Ответ на стикер
  if message.sticker:
      bot.send_message(message.chat.id, 'Вы отправили стикер.')

bot.polling()