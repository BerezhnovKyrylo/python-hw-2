# Напишіть функцію commonStr що задовільняє наступній умові:

# Дано дві строчки, поверніть нову строчку
# яка буде складатись виключно зі спільних символів перерадних строк.
# Якщо немає спільних символів - поверніть пусту строчку.
# Ви можете повернути відповідь у будь-якому порядку.
# Символи не повині дублюватись у відповіді.

# Приклад 1
# commonStr('loli', 'luck') -> 'l'

# Приклад 1
# commonStr('good day', 'good morning') -> 'god'

def commonStr(str):
    print(''.join([i if i in set(str[0]) else '' for i in set(str[1])]))
    return 1
if __name__ == '__main__':
    commonStr([input(f'Введите строку {i+1}: ') for i in range(2)])