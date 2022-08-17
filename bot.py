import telebot
from config import TOKEN
import keyboard as kb
import funcs


bot = telebot.TeleBot(TOKEN)  #Регистрация бота в переменную bot


@bot.message_handler(commands=['start'])  #Реакция на команду /start
def start(message):
    bot.send_message(message.chat.id, f"Здраствуйте, {message.chat.first_name} 👋\nВыберите какаие новости вас интересуют 👇", reply_markup=kb.main_markup)


@bot.message_handler(content_types=["text"])  #Обработчик текстовых сообщений
def main(message):
    if message.text == "📄 РИА":
        news = funcs.parse_ria()  #Функция возвращает список из названий и ссылок новостей
        for new in news:
            try:
                bot.send_message(message.chat.id,'<a href="{}">{}</a>'.format(new[1], new[0]), parse_mode='html')
            except:
                pass
        bot.send_message(message.chat.id,"👆 Это все новости на данный момент")
    elif message.text == "🎬 КИНО":
        news = funcs.parse_kino()  #Функция возвращает список из названий и ссылок новостей
        for new in news:
            try:
                bot.send_photo(message.chat.id,photo=open("images/kinopoisk.png", "rb"), caption='<a href="{}">{}</a>'.format(new[1], new[0]), parse_mode='html')
            except:
                pass
        bot.send_message(message.chat.id,"👆 Это все новости на данный момент")
    elif message.text == "⚽️ CПОРТ":
        news = funcs.parse_sport()  #Функция возвращает список из названий и ссылок новостей
        for new in news:
            try:
                bot.send_message(message.chat.id,'<a href="{}">{}</a>'.format(new[1], new[0]), parse_mode='html')
            except:
                pass
        bot.send_message(message.chat.id,"👆 Это все новости на данный момент")
    elif message.text == "🎮 ВИДЕОИГРЫ":
        news = funcs.parse_games()  #Функция возвращает список из названий и ссылок новостей
        for new in news:
            try:
                bot.send_message(message.chat.id,'<a href="{}">{}</a>'.format(new[1], new[0]), parse_mode='html')
            except:
                pass
        bot.send_message(message.chat.id,"👆 Это все новости на данный момент")
    elif message.text == "🖥 ТЕХНОЛОГИИ":
        news = funcs.parse_tecnology()  #Функция возвращает список из названий и ссылок новостей
        for new in news:
            try:
                bot.send_message(message.chat.id,'<a href="{}">{}</a>'.format(new[1], new[0]), parse_mode='html')
            except:
                pass
        bot.send_message(message.chat.id,"👆 Это все новости на данный момент")
    else:
        bot.reply_to(message, "⚠️ Неизвестная команда")  #Бот отвечвет на неизвестную команду

            
 






bot.polling(none_stop=True)
