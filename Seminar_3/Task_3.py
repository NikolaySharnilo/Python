#3. Генератор псевдослучайных чисел
import datetime

now = datetime.datetime.now()

print(now.microsecond // 10000)

