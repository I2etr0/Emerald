import telebot
from telebot import types
from file import stoken  # Предполагается, что stoken содержит токен бота

token = stoken
bot = telebot.TeleBot(f'{token}')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создание кнопок первого уровня
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Получить ID', callback_data='get_id')
    button2 = types.InlineKeyboardButton('Перейти к ИИ', callback_data='get_ii')
    keyboard.row(button1, button2)

    # Отправка сообщения с клавиатурой
    bot.send_message(
        message.chat.id,
        'Привет! Меня зовут Эмеральд. Чем я могу тебе помочь?',
        reply_markup=keyboard
    )

# Обработчик команды /id
@bot.message_handler(commands=['id'])
def handle_id(message):
    bot.send_message(
        message.chat.id,
        f'<b> <code>{message.from_user.id}</code> </b> - это Ваш ID, но учтите, что его надо держать в секрете!!!',
        parse_mode='HTML'
    )

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_id(message):
    bot.send_message(
        message.chat.id,
        'Привет! Ты вызвал эту подсказку. Вот что может этот бот:\n'
        '/start - запустить бота\n'
        '/help - вызвать эту подсказку\n'
        '/id - вывести в чат твой ID аккаунта.',
        parse_mode='HTML'
    )

# Обработчик нажатия на inline-кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'get_id':
        user_id = call.from_user.id
        bot.send_message(
            call.message.chat.id,
            f'<b> <code>{user_id}</code> </b> - это Ваш ID, но учтите, что его надо держать в секрете!!!',
            parse_mode='HTML'
        )

    elif call.data == 'get_ii':
        # Создание клавиатуры для выбора ИИ
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        button3 = types.InlineKeyboardButton('Qwen', url='https://chat.qwen.ai')
        button4 = types.InlineKeyboardButton('DeepSeek к ИИ', url='https://chat.deepseek.com')
        button5 = types.InlineKeyboardButton('Назад', callback_data='back')
        keyboard.add(button3, button4)
        keyboard.row(button5)

        # Изменение сообщения с новой клавиатурой
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите нужный ИИ:',
            reply_markup=keyboard
        )

    elif call.data == 'back':
        # Возвращение к начальному меню
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Получить ID', callback_data='get_id')
        button2 = types.InlineKeyboardButton('Перейти к ИИ', callback_data='get_ii')
        keyboard.row(button1, button2)

        # Изменение сообщения с начальной клавиатурой
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Привет! Меня зовут Эмеральд. Чем я могу тебе помочь?',
            reply_markup=keyboard
        )

# Запуск бота
bot.polling(non_stop=True)