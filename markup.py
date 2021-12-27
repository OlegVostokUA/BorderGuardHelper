from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ---------------------------------------------------------- #
buttonStart = KeyboardButton('/start')
buttonRead = KeyboardButton('/readme')
grandMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(buttonStart, buttonRead)

#buttonMain = KeyboardButton('Главное меню')


#-----Start menu------#

buttonGroups = KeyboardButton('Елем. Сл. Пор.')
buttonCalculations = KeyboardButton('/Розрахунки')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(buttonGroups, buttonStart, buttonCalculations, buttonRead)

#----Groups menu-----#
button1 = KeyboardButton('Група Прик ДК')
button2 = KeyboardButton('Група Прик ОН')
button3 = KeyboardButton('Група Пошуку')
button4 = KeyboardButton('Вогнева група')
button5 = KeyboardButton('Група СП')
button6 = KeyboardButton('Резерв')
button7 = KeyboardButton('Схема СЗ. (ВАРІАНТ)')
groupsMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(button1, button2, button3, button4, button5, button6, button7, buttonStart)

#-----Ca-ns menu-----#
buttonCalc = KeyboardButton ('/РОЗРАХУВАТИ')
calcMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonCalc, buttonStart)