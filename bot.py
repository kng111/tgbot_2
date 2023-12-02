import telebot
import datetime
import random
import time
import sqlite3

bot_token = '6297955354:AAGN-1mDkpxFcviDRyZJ6qwuNj596zTCKhU'
bot = telebot.TeleBot(token=bot_token)
db = sqlite3.connect('DR_Koll.db')
cur = db.cursor()

def dr():
        cur.execute('SELECT imy,fam,otch,doljn FROM table1 where dr = "31:08"')
        result = cur.fetchall()
        result = result[0]
        # print(result,sep='\n')
        l = (' '.join(map(str,result )))
        # x2 = (str(l)[1:-2])
        return l
fio = dr()

def pozdr():
        cur.execute('SELECT pozdr from table2')
        result = cur.fetchall()
        result = random.choice(result)
        # print(result,sep='\n')

        l = (' '.join(map(str,result )))
        # x2 = (str(l)[1:-2])
        # l = random.choice(l)
        return l
pozdrv = pozdr()
# print(pozdrv)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для отправки поздравлений. Напишите /congratulate, чтобы получить поздравление.")

@bot.message_handler(commands=['congratulate'])
def send_congratulation(message):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S") # "%Y-%m-%d %H:%M":%S
        print((current_time))
        # if current_time == "21:35:59":
        list_random = [ '\U0001F3B2','\U0001F947','\U00002600','\U0001FA84','\U00002728','\U0001F389','\U0001F396','\U0001F4A1']
        bot.reply_to(message, f"\U0001F916:{fio},{pozdrv} Текущее время: {current_time} {random.choice(list_random)} ")

bot.polling()
