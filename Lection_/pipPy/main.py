from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token('5611156496:AAGTrs3cZZMERerFKmJYWLLfflBUsu87Db8').build()

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print("Ок")
app.run_polling()






# import matplotlib.pyplot as plt
# import numpy as np



# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()


# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))


# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()



#from isOdd import isOdd

#print(isOdd(1)) 
#print(isOdd(0)) 