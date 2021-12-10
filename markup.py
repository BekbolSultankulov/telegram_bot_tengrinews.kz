from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


mainLearn=KeyboardButton('Узнай')
mainRead=KeyboardButton('Почитай')
mainWatch=KeyboardButton('Посмотри')
mainMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(mainLearn,mainRead,mainWatch)



btnMain=KeyboardButton('главное')

today=KeyboardButton('сегодня')
yesterday=KeyboardButton('вчера')
dayBtn=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(today,yesterday,btnMain)





