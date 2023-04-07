ANUM = 4
ANUMPR = 4
import apiclient.discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
import telebot
from telebot import types
from datetime import datetime

ids = [1144292157]
bot = telebot.TeleBot("5867116281:AAH6zMU3ouNhdQF4_tA6sQ1RdikfaYHxckk")
CREDENTIALS_FILE = 'leafy-ether-382619-94d1b8bb4a78.json'  # Имя файла с закрытым ключом, вы должны подставить свое
spreadsheetId = "1VSnFajWGEM7_-FngJcdWw24BZ4RwtIsZxkyVy5IAy0g"
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API

@bot.message_handler(commands=['start', 'help'])
def start(message):
    global ids  # массив с ID
    if message.from_user.id not in ids:
        bot.send_message(message.chat.id, 'Ошибся адресом, дружок')
    else:
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Расходы")
        item2 = types.KeyboardButton("Приходы")
        murkup.add(item1, item2)
        bot.send_message(message.chat.id, "Выбери", reply_markup=murkup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global ANUM
    global spreadsheetId
    global CREDENTIALS_FILE
    global ids  # массив с ID
    if message.from_user.id not in ids:
        bot.send_message(message.chat.id, 'Ошибся адресом, дружок')
    else:
        if message.chat.type == 'private':
            if message.text == 'Расходы':
                murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Семья")
                item2 = types.KeyboardButton("Кондитерка")
                murkup.add(item1, item2)
                bot.send_message(message.chat.id, "Расходы", reply_markup=murkup)

            if message.text == 'Приходы':
                murkup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                Nal = types.KeyboardButton("Наличка")
                Cardbel = types.KeyboardButton("Карта(Беларусьбанк)")
                Cardprior = types.KeyboardButton("Карта(Приорбанк)")
                murkup2.add(Nal, Cardbel, Cardprior)
                sent = bot.send_message(message.chat.id, "Куда поступление?", reply_markup=murkup2)
                bot.register_next_step_handler(sent, Prihod)

            elif message.text == 'Семья':
                murkup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                Nal = types.KeyboardButton("Наличка")
                Cardbel = types.KeyboardButton("Карта(Беларусьбанк)")
                Cardprior = types.KeyboardButton("Карта(Приорбанк)")
                murkup2.add(Nal, Cardbel, Cardprior)
                sent = bot.send_message(message.chat.id, "Откуда списание?", reply_markup=murkup2)
                bot.register_next_step_handler(sent, Fam)

            elif message.text == 'Кондитерка':
                murkup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                Nal = types.KeyboardButton("Наличка")
                Cardbel = types.KeyboardButton("Карта(Беларусьбанк)")
                Cardprior = types.KeyboardButton("Карта(Приорбанк)")
                murkup2.add(Nal, Cardbel, Cardprior)
                sent = bot.send_message(message.chat.id, "Откуда списание?", reply_markup=murkup2)
                bot.register_next_step_handler(sent, Cond)


def Prihod(message):
    global ids  # массив с ID
    if message.from_user.id not in ids:
        bot.send_message(message.chat.id, 'Ошибся адресом, дружок')
    else:
        if message.text == 'Наличка':
            sent = bot.send_message(message.chat.id, "Имя клиента")
            bot.register_next_step_handler(sent, PrihodNal)

        elif message.text == 'Карта(Беларусьбанк)':
            sent = bot.send_message(message.chat.id, "Имя клиента")
            bot.register_next_step_handler(sent, PrihodBel)

        elif message.text == 'Карта(Приорбанк)':
            sent = bot.send_message(message.chat.id, "Имя клиента")
            bot.register_next_step_handler(sent, PrihodPrior)


def Fam(message):
    global ids  # массив с ID
    if message.from_user.id not in ids:
        bot.send_message(message.chat.id, 'Ошибся адресом, дружок')
    else:
        if message.text == 'Наличка':
            sent = bot.send_message(message.chat.id, "На что потратили")
            bot.register_next_step_handler(sent, FamNal)

        elif message.text == 'Карта(Беларусьбанк)':
            sent = bot.send_message(message.chat.id, "На что потратили")
            bot.register_next_step_handler(sent, FamBel)

        elif message.text == 'Карта(Приорбанк)':
            sent = bot.send_message(message.chat.id, "На что потратили")
            bot.register_next_step_handler(sent, FamPrior)


def Cond(message):
    global ids  # массив с ID
    if message.from_user.id not in ids:
        bot.send_message(message.chat.id, 'Ошибся адресом, дружок')
    else:
        if message.text == 'Наличка':
            sent = bot.send_message(message.chat.id, "На что потратили")
            bot.register_next_step_handler(sent, CondNal)

        elif message.text == 'Карта(Беларусьбанк)':
            sent = bot.send_message(message.chat.id, "На что потратили")
            bot.register_next_step_handler(sent, CondBel)

        elif message.text == 'Карта(Приорбанк)':
            sent = bot.send_message(message.chat.id, "На что потратили")
            bot.register_next_step_handler(sent, CondPrior)


# Приходы
def PrihodNal(message):
    global ANUMPR
    current_datetime = datetime.now()
    Name = message.text
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Name]
    sent = bot.send_message(message.chat.id, "Сколько получили?")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!J" + str(ANUMPR) + ":K400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, PrihodNalPlus)


def PrihodBel(message):
    global ANUMPR
    current_datetime = datetime.now()
    Name = message.text
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Name]
    sent = bot.send_message(message.chat.id, "Сколько получили?")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!J" + str(ANUMPR) + ":K400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, PrihodBelPlus)


def PrihodPrior(message):
    global ANUMPR
    Name = message.text
    current_datetime = datetime.now()
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Name]
    sent = bot.send_message(message.chat.id, "Сколько получили?")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!J" + str(ANUMPR) + ":K400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, PrihodPriorPlus)


def PrihodNalPlus(message):
    global ANUMPR
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!L" + str(ANUMPR) + ":L400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUMPR += 1


def PrihodBelPlus(message):
    global ANUMPR
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!M" + str(ANUMPR) + ":M400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUMPR += 1


def PrihodPriorPlus(message):
    global ANUMPR
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!N" + str(ANUMPR) + ":N400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUMPR += 1


# Семья расходы
def FamNal(message):
    current_datetime = datetime.now()
    Why = message.text
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Why]
    sent = bot.send_message(message.chat.id, "Сколько потратили:")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!A" + str(ANUM) + ":B400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, FamNalmines)


def FamBel(message):
    Why = message.text
    current_datetime = datetime.now()
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Why]
    sent = bot.send_message(message.chat.id, "Сколько потратили:")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!A" + str(ANUM) + ":B400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, FamBelmines)


def FamPrior(message):
    current_datetime = datetime.now()
    Why = message.text
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Why]
    sent = bot.send_message(message.chat.id, "Сколько потратили:")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!A" + str(ANUM) + ":B400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, FamPriormines)


def FamNalmines(message):
    global ANUM
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!C" + str(ANUM) + ":C400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUM += 1


def FamBelmines(message):
    global ANUM
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!D" + str(ANUM) + ":D400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUM += 1


def FamPriormines(message):
    global ANUM
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!E" + str(ANUM) + ":E400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUM += 1


# Кондитерка расходы
def CondNal(message):
    current_datetime = datetime.now()
    Why = message.text
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Why]
    sent = bot.send_message(message.chat.id, "Сколько потратили:")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!A" + str(ANUM) + ":B400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, CondNalmines)


def CondBel(message):
    current_datetime = datetime.now()
    Why = message.text
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Why]
    sent = bot.send_message(message.chat.id, "Сколько потратили:")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!A" + str(ANUM) + ":B400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, CondBelmines)


def CondPrior(message):
    current_datetime = datetime.now()
    Why = message.text
    mas = [str(current_datetime.day) + "." + str(current_datetime.month) + "." + str(current_datetime.year) + " " + str(current_datetime.hour) + ':' + str(current_datetime.minute), Why]
    sent = bot.send_message(message.chat.id, "Сколько потратили:")
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!A" + str(ANUM) + ":B400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    bot.register_next_step_handler(sent, CondPriormines)


def CondNalmines(message):
    global ANUM
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!F" + str(ANUM) + ":F400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUM += 1


def CondBelmines(message):
    global ANUM
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!G" + str(ANUM) + ":G400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUM += 1


def CondPriormines(message):
    global ANUM
    mines = message.text
    mas = [mines]
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист номер один!H" + str(ANUM) + ":H400",
             "majorDimension": "ROWS",
             "values": [mas]}
        ]
    }).execute()
    OK(message)
    ANUM += 1


def OK(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Расходы")
    item2 = types.KeyboardButton("Приходы")
    murkup.add(item1, item2)
    bot.send_message(message.chat.id, "Записанно", reply_markup=murkup)


bot.infinity_polling()
