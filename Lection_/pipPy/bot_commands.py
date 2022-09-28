
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
import datetime


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = (f'hi {update.effective_user.first_name}')
    log(update, context, answer)
    await update.message.reply_text(f'{answer}')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = (f'{datetime.datetime.now().time()}')
    log(update, context, answer)
    await update.message.reply_text(f'{answer}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = (f'/hello\n/time\n/help\n/sum')
    log(update, context, answer)
    await update.message.reply_text(f'{answer}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split(' ')
    sum = int(items[1]) + int(items[2])
    answer = (f'result:{items[1]} + {items[2]} -> {sum}')
    log(update, context, answer)
    await update.message.reply_text(f'{answer}')

