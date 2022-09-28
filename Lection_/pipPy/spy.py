from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

def log(update: Update, context: ContextTypes.DEFAULT_TYPE, answer):
    path = '/Users/user/Desktop/Разработчик/Python/Lection_/pipPy'
    file = open(f'{path}/db.csv', 'a', encoding='utf-8')
    answer = answer.replace('\n',' $ ')
    file.write(f'{datetime.datetime.now()}; {update.effective_user.first_name}; {update.effective_user.id}; {update.message.text}; {answer}\n')
    file.close()
