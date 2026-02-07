import builtins
from time import sleep
import sys

BUILT_IN_FLAGS = BUILT_IN_FLAGS or {}

builtins.длина = len
builtins.диапазон = range
builtins.макс = max
builtins.мин = min
builtins.вывести = print
builtins.лист = list
builtins.число = int
builtins.дробь = float
builtins.строка = str

builtins.модуль = abs
builtins.сумма = sum
builtins.степень = pow
builtins.округ = round
builtins.открыть = open
builtins.энумерировать = enumerate
builtins.подождать = sleep
builtins.ввод = input

builtins.нет = False
builtins.ложь = False

builtins.да = True
builtins.истина = True

builtins.новая_строка = "\n"

class RuOutput:
    def __init__(self, stream):
        self.stream = stream
    def write(self, data: str):
        data = data.replace('True', 'Да' if BUILT_IN_FLAGS.get("USE_YES_NOT_TRUE") else 'Истина').replace('False', 'Нет' if BUILT_IN_FLAGS.get("USE_YES_NOT_TRUE") else 'Ложь')
        self.stream.write(data)
    def flush(self):
        self.stream.flush()

sys.stdout = RuOutput(sys.stdout)