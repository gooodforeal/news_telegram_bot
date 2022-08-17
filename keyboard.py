from telebot import types


'''                      MAIN MENU                        '''
main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    #Клавиатура главного меню
main_markup.row('📄 РИА', '🎬 КИНО', "⚽️ CПОРТ")
main_markup.row('🎮 ВИДЕОИГРЫ', "🖥 ТЕХНОЛОГИИ")
