from os import error
import telebot
import os.path
import test_catalog_response
import traceback
import api_catalog
from urllib.parse import urlparse
bot = telebot.TeleBot('1002235927:AAGrXDX5GddG-ddYKcKb_MWeH_fVJklB8s0', num_threads=100)

white_list = [723817809, 1250963887, 691046923,265696327,996842560]
allow_id = {item for item in white_list}
new_catalog_all = []

def runner(handler):
    def _handler(message):
        try:
            handler(message)
        except Exception as error:
            bot.send_message(message.chat.id, traceback.format_exc())

    return _handler


def file_status(message,status = None):
    test=f'{str(message.from_user.id)}.txt'
    test1=f'{str(message.from_user.id)}+all_catalog.txt'
    
    test_catalog_response.catalog_respose.filename_user_catalog = test1
    test_catalog_response.catalog_respose.filename_user = test 
    if status is None:
       return  test1
    return  test



def status_bar(msg, cid, message):
    while  os.path.isfile(file_status(message,1)) == True:
        status = test_status(message)
        if status is None:
            continue
        status = status + f"/{len(new_catalog_all)}"
        if status == msg.html_text:
            continue
        #{len(new_catalog_all)}
        msg = bot.edit_message_text(chat_id=cid, message_id=msg.message_id, text = f"{test_status(message)}/{len(new_catalog_all)}" )        
        cid = msg.chat.id
        if test_status(message)==len(new_catalog_all)/2:
            file1 = open(file_status(message), 'rb')
            bot.send_document(message.chat.id, file1)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),file_status(message)))


                       
       
def test_status(message):
    if os.path.isfile(file_status(message,1)) == True:
        test = None      
        my_file = open(file_status(message,1), "r")
        for i in my_file:
            test = i
        my_file.close()    
        return test

def catalog(test,test1=None):
    catalog_bot = {"Телефоны и гаджеты":"/catalog/portativ/",
                    "Компьютерная техника":"/catalog/computers/",
                    "Офисная техника и сети":"/catalog/network/",
                    "Телевизоры, аудио, видео":"/catalog/audio-video/",
                    "Климатическая техника":"/catalog/climate_control/",
                    "Бытовая техника":"/catalog/appliance/",
                    "Красота, здоровье":"/catalog/beauty/",
                    "Спорт, одежда, хобби":"/catalog/sport/",
                    "Бытовая химия и гигиена":"/catalog/bytovaya_himiya_i_gigiena/",
                    "Книги, канцтовары, хобби":"/catalog/knigi_i_kanctovary/",
                    "Фото- и видеокамеры":"/catalog/cameras/",
                    "Игры и развлечения":"/catalog/games/",
                    "Товары для дома":"/catalog/remont/",
                    "Автомобильная техника":"/catalog/avtomobilynaya_tehnika/",
                    "Уцененные товары":"/catalog/ucenka/"}
    if test1 == True:
        for key, value in catalog_bot.items():
            if key ==test:                
                return value 
    else:                    
        for key, value in catalog_bot.items():
            if key ==test:                
                return key                


           
@bot.message_handler(commands=['test'],func=lambda message: message.chat.id   in allow_id)
@runner
def first_button(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    item1 = telebot.types.KeyboardButton('Выполнить поиск по всем каталогам')
    item2 = telebot.types.KeyboardButton('Получить результат')
    item3 = telebot.types.KeyboardButton('Весь каталог')
    item4 = telebot.types.KeyboardButton('Остановить работу')
    item5 = telebot.types.KeyboardButton('Status')
    item6 = telebot.types.KeyboardButton('restart token')
    keyboard.add(item4,item2,item3,item5,item6,item1)
    bot.send_message(message.chat.id, 'Меню', reply_markup=keyboard)
@bot.message_handler(commands=['stop'],func=lambda message: message.chat.id   in allow_id)
@runner
def stop(message):
    bot.send_message(message.chat.id, 'Stop work')
    if os.path.isfile(file_status(message,1)) == True:
        test_catalog_response.catalog_respose.stop_bot = 1
            
    if os.path.isfile(file_status(message)) == False:
            bot.send_message(message.from_user.id, "Результаты отсутствуют запустите скрипт /help")
    if os.path.isfile(file_status(message)) == True:
        file1 = open(file_status(message), 'rb')
        try:
            bot.send_document(message.chat.id, file1)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),file_status(message)))
        except:
            pass    
        

@bot.message_handler(commands=['all_catalog'])
@runner
def all_catalog(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    item1 = telebot.types.KeyboardButton('Телефоны и гаджеты')
    item2 = telebot.types.KeyboardButton('Компьютерная техника')
    item3 = telebot.types.KeyboardButton('Офисная техника и сети')
    item4 = telebot.types.KeyboardButton('Телевизоры, аудио, видео')
    item5 = telebot.types.KeyboardButton('Климатическая техника')
    item6 = telebot.types.KeyboardButton('Бытовая техника')
    item7 = telebot.types.KeyboardButton('Красота, здоровье')
    item8 = telebot.types.KeyboardButton('Спорт, одежда, хобби')
    item9 = telebot.types.KeyboardButton('Бытовая химия и гигиена')
    item10 = telebot.types.KeyboardButton('Книги, канцтовары, хобби')
    item11 = telebot.types.KeyboardButton('Фото- и видеокамеры')
    item12 = telebot.types.KeyboardButton('Игры и развлечения')
    item13 = telebot.types.KeyboardButton('Товары для дома')
    item14 = telebot.types.KeyboardButton('Автомобильная техника')
    item15 = telebot.types.KeyboardButton('Уцененные товары')
    item16 = telebot.types.KeyboardButton('Back')
    item17 = telebot.types.KeyboardButton('Остановить работу')
    item18 = telebot.types.KeyboardButton('Status')
    keyboard.add(item1, item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18)
    bot.send_message(message.chat.id,'Весь Каталог', reply_markup=keyboard)    

@bot.message_handler(commands=['status'],func=lambda message: message.chat.id   in allow_id)
@runner
def status(message):

    cid = message.chat.id
    if os.path.isfile(file_status(message,1)) == False:
        bot.send_message(message.from_user.id, "Скрипт закончил работу или не запускался проверьте")
    if os.path.isfile(file_status(message,1)) == True:
        
        msg = bot.send_message(message.from_user.id, f"Результат скрипта")
       
        status_bar(msg,cid,message)
               
   
@bot.message_handler(commands=['start'])
@runner
def start(message):
    user_id = message.from_user.id
    bot.send_message(message.from_user.id, 'Бот компании 05.ru является собсвтенностью компании любые не законные действия приведут к последствиям')
    bot.send_message(message.from_user.id, 'Лан шучу удачного пользования! Пиши /help')  
    bot.send_message(message.from_user.id,'Если кнопки не работают можешь написать в ручную или обратиться к @mu_r_zik')   
    bot.send_message(message.from_user.id, f'{user_id}')
    first_button(message) 

@bot.message_handler(content_types=['text'] ,func=lambda message: message.chat.id   in allow_id )
@runner
def get_text_messages(message):
    link = message.json["text"]
    link_host =urlparse(link).hostname 
    link_scheme = urlparse(link).scheme
    global new_catalog_all
    if message.text == "/help":
        bot.send_message(message.from_user.id, "/test /status /all_catalog /start /stop")
    elif message.text == "Выполнить поиск по всем каталогам" :
        if os.path.isfile(file_status(message,1)) == True:
            bot.send_message(message.from_user.id, "Скрипт уже запущен ожидайте")
            bot.send_message(message.from_user.id, "Для проверки статуса введите /status")   
        else:
            bot.send_message(message.from_user.id, "Скрипт запущен")
            new_catalog_all = test_catalog_response.catalog_all
            test_catalog_response.catalog_respose.start()
            cid = message.chat.id
            msg = bot.send_message(message.from_user.id, f"Результат скрипта")
            status_bar(msg,cid,message)
               
    elif message.text == 'Получить результат':
        if os.path.isfile(file_status(message)) == False:
            bot.send_message(message.from_user.id, "Результаты отсутствуют запустите скрипт /help")
        if os.path.isfile(file_status(message)) == True:
            file1 = open(file_status(message), 'rb')
            bot.send_document(message.chat.id, file1)
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),file_status(message)))
    elif link_host== "05.ru" and (link_scheme == "https" or link_scheme == "http"):
        file_status(message)
        bot.send_message(message.from_user.id,f"вами введена следующая ссылка {link}") 
        bot.send_message(message.from_user.id,"идет поиск товаров в выбранной ссылке")
       
        test_catalog_response.Test_bot.bot(message.html_text, new_catalog_all)
    elif message.text == 'Весь каталог':
        all_catalog(message)
    elif message.text == 'Остановить работу':
        stop(message)
        if os.path.isfile(file_status(message,1))==True:
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),file_status(message,1)))
    elif message.text == catalog(message.text):
        if os.path.isfile(file_status(message,1)) == True:
            bot.send_message(message.from_user.id, "Скрипт уже запущен ожидайте")
            bot.send_message(message.from_user.id, "Для проверки статуса введите /status")
            
        else:
            file_status(message,1)
            test = catalog(message.text,1)
            bot.send_message(message.from_user.id ,"Каталог найден идет запуск скрипта")
            test_catalog_response.Test_bot.bot(test, new_catalog_all)
            
            if os.path.isfile(file_status(message))==True:
                file1 = open(file_status(message), 'rb')
                bot.send_document(message.chat.id, file1)
                os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),file_status(message)))
    elif message.text == 'Back':
        first_button(message)
    elif message.text == 'Status':
        status(message)
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Back')
        keyboard.add(item1)
    elif message.text == 'restart token':
        api_catalog.Token_api.restart_token()

    else:
        bot.send_message(message.from_user.id, "Пиши /help.")




if __name__ == '__main__':
    bot.polling(none_stop=True)




