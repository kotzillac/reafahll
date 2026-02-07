import tokenize
import io
from pathlib import Path
from sys import argv

BUILT_IN_FLAGS = {}

class ИноагентОшибка(Exception):
    pass

"""
Компилятор русского легкого анти-иноагентского выскоуровнего языка

|**************************************************|
|АВТОРЫ: [kotzillac](https://github.com/kotzillac) |
|ССЫЛКА: https://github.com/kotzillac/reafahll/rupy|
|**************************************************|
"""

ДИРЕКТОРИЯ_СКРИПТА = Path(__file__).parent 
СЛОВАРЬ = {'для': 'for', "в": 'in', 'пока': 'while', 'если': 'if', 'иначе': 'else', 'иначе_если': 'elif', 'функция': 'def', 'вернуть': 'return'}

БАЗОВЫЙ_ТЕКСТ = """\n
\"\"\"
ДАННЫЙ КОД СДЕЛАН АВТОМАТИЧЕСКИМ КОМПИЛЯТОРОМ РЛАИАВУЯ
И НЕ РЕКОМЕНДУЕТСЯ К ИЗМЕНЕНИЯМ
\"\"\"

\"\"\"
Русский легкий анти-иноагентский высокоуровневый язык

|**************************************************|
|АВТОРЫ: [kotzillac](https://github.com/kotzillac) |
|ССЫЛКА: https://github.com/kotzillac/reafahll/rupy|
|**************************************************|
\"\"\"
\n
""" + Path(ДИРЕКТОРИЯ_СКРИПТА / "rubuiltins.py").read_text(encoding="utf-8") + "\n\n"

def скомпелировать_РЛАИАВУЯ(код: str):
    токены = tokenize.tokenize(io.BytesIO(код.encode("utf-8")).readline)
    результат = []

    if код and "#! МЕССЕНДЖЕР МАКС" not in код:
        raise ИноагентОшибка("Вы не признались в любви родине!")

    for тип, текст, _, _, _ in токены:
        if тип == tokenize.NAME and текст in СЛОВАРЬ:
            результат.append((тип, СЛОВАРЬ[текст]))
        elif (тип == tokenize.NAME and текст == "то") or (тип == tokenize.NAME and текст == "делать"):
            результат.append((tokenize.OP, ":"))
        else:
            результат.append((тип, текст))
    
    return БАЗОВЫЙ_ТЕКСТ + tokenize.untokenize(результат).decode("utf-8")

def выполнить_РЛАИАВУЯ(путь_до_файла: Path | str,
        сохранять_промежуточный_файл: bool = False):

    путь_до_файла = Path(путь_до_файла)

    if путь_до_файла.is_absolute != True:
        путь_до_файла = ДИРЕКТОРИЯ_СКРИПТА / путь_до_файла
    
    код = путь_до_файла.read_text(encoding="utf-8")
    промежуточный_код = скомпелировать_РЛАИАВУЯ(код)

    if сохранять_промежуточный_файл:
        (путь_до_файла.parent / Path(путь_до_файла.stem + ".compiled.rupy.py")).write_text(промежуточный_код, encoding="utf-8")
    exec(промежуточный_код, globals(), globals())

if __name__ == '__main__':
    args = argv[1:]
    промежуточный_код = "-ir" in args

    if "-flags" in args:
        try:
            flags_id = args.index("-flags")
            flags_str = args[flags_id + 1]
            BUILT_IN_FLAGS = dict(item.split("=") for item in flags_str.split(","))
            for flag_key, flag_value in BUILT_IN_FLAGS.items():
                if flag_value.lower() == "true":
                    BUILT_IN_FLAGS[flag_key] = True
                elif flag_value.lower() == "false":
                    BUILT_IN_FLAGS[flag_key] = False
                else:
                    try:
                        BUILT_IN_FLAGS[flag_key] = float(flag_value)
                    except ValueError:
                        continue
        except (IndexError, ValueError):
            raise SyntaxError("После -flags должно идти значение")
    
    flags_str_id = args.index("-flags") + 1 if "-flags" in args else -1

    try:
        путь_файла = [arg for i, arg in enumerate(args) 
                      if arg != "-ir" and arg != "-flags" and i != flags_str_id][0]
        выполнить_РЛАИАВУЯ(путь_файла, промежуточный_код)
    except IndexError:
        raise FileNotFoundError("Не найден путь до файла в аргументах!")