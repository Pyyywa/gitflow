def func(word):
    "Функция делает все буквы заглавными"
    return word.upper()

def func2(word):
    "Функция делает заглавными первые буквы слова"
    return word.title()


line = input('Введите строку')
print(func(line))
print(func2(line))